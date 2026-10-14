# ============================================================
#  inpi_scraper.py — Catalogador de Patentes INPI (Brasil)
# ============================================================
#
#  Pode ser usado de duas formas:
#    1. Standalone:  python inpi_scraper.py
#       → salva em EXCEL_SAIDA / REVISAO_SAIDA / PASTA_PDF
#
#    2. Integrado via main.py (opção 5):
#       → main.py importa as funções e redireciona para
#         patents_data_test.xlsx / Patentes/ do sistema principal
#
#  Fluxo do site INPI:
#    página inicial → "Continuar" → "Patente" → formulário
#    → resultado → detalhe → extração → download PDF (JS)
#
#  Dependências:
#    pip install selenium pandas openpyxl beautifulsoup4
#
# ============================================================

import os
import re
import sys
import time
import shutil
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, WebDriverException
)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ─────────────────────────────────────────────────────────────
#  CONFIGURAÇÃO — edite aqui ao usar standalone
# ─────────────────────────────────────────────────────────────

CODIGOS_INPI = [
    "PI0707169-8",
    "MU8202153-8",
    "PI0403519-4",
    "PI0005164-0",
    "PI0113728-0",
    # Adicione mais códigos aqui
]

# Quando rodado standalone, salva nestes arquivos/pasta.
# Quando chamado pelo main.py, esses valores são ignorados —
# o main.py passa seus próprios caminhos.
EXCEL_SAIDA   = "inpi_data.xlsx"
REVISAO_SAIDA = "inpi_revisao.xlsx"
PASTA_PDF     = "PDFs_INPI"      # pasta temporária; main.py move para Patentes/
BAIXAR_PDFS   = True

URL_INPI = "https://busca.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp"

# Colunas idênticas ao Google Patents scraper para facilitar unificação
COLUNAS = [
    "Código", "Código Pesquisado", "Local", "Título",
    "Assignee", "Inventores", "Current Assignee",
    "Filed Date", "First Publication Date", "Issue Date",
    "Abstract", "Nome do Arquivo",
    "Assunto Primario", "Assunto Secundario", "Assunto Terciario",
]


# ─────────────────────────────────────────────────────────────
#  NORMALIZAÇÃO
# ─────────────────────────────────────────────────────────────

def normalizar_codigo(codigo):
    """
    Remove espaços, hífens e sufixos de tipo para busca no INPI.
    "PI 0707169-8 A2" → "PI07071698"
    "MU 8202153-8"    → "MU82021538"
    """
    codigo = codigo.strip().upper()
    codigo = re.sub(r'\s+[AB]\d\s*$', '', codigo)   # remove A1, A2, B1...
    codigo = re.sub(r'[\s\-\.]', '', codigo)
    return codigo


# ─────────────────────────────────────────────────────────────
#  DRIVER
# ─────────────────────────────────────────────────────────────

def setup_driver():
    """
    Chrome visível — necessário para o INPI (detecta headless)
    e para permitir resolução manual de CAPTCHA.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=pt-BR")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")

    # Download automático de PDFs sem diálogo
    prefs = {
        "download.default_directory": os.path.abspath(PASTA_PDF),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    # Oculta flag webdriver para reduzir chance de bloqueio
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
    )
    driver.set_page_load_timeout(30)
    return driver


def reiniciar_driver(driver):
    try:
        driver.quit()
    except Exception:
        pass
    time.sleep(1)
    print("  [Driver reiniciado]")
    return setup_driver()


# ─────────────────────────────────────────────────────────────
#  CAPTCHA — detecção por elemento visível, não por HTML
# ─────────────────────────────────────────────────────────────

def verificar_e_resolver_captcha(driver):
    """
    Pausa o script se um CAPTCHA visível for detectado.
    Ignora menções à palavra "captcha" no código-fonte (falso positivo comum).
    """
    try:
        seletores = [
            "iframe[src*='recaptcha']",
            "iframe[src*='captcha']",
            "div.g-recaptcha",
            "div[class*='captcha']",
            "#captcha",
            "input[name*='captcha']",
        ]
        for sel in seletores:
            for el in driver.find_elements(By.CSS_SELECTOR, sel):
                if el.is_displayed():
                    _pausar_captcha()
                    return True

        # Verifica texto visível (não HTML)
        texto = driver.find_element(By.TAG_NAME, "body").text.lower()
        if any(f in texto for f in ["não sou um robô", "i'm not a robot",
                                     "verificação de segurança"]):
            _pausar_captcha()
            return True

    except Exception:
        pass
    return False


def _pausar_captcha():
    print("\n" + "=" * 55)
    print("  ⚠  CAPTCHA DETECTADO!")
    print("  Resolva o CAPTCHA na janela do Chrome.")
    print("  Depois volte aqui e pressione ENTER para continuar.")
    print("=" * 55)
    input("  [Pressione ENTER após resolver o CAPTCHA] ")
    time.sleep(1)


# ─────────────────────────────────────────────────────────────
#  NAVEGAÇÃO
# ─────────────────────────────────────────────────────────────

def _esperar(driver, by, selector, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )
    except TimeoutException:
        return None


def _clicar(driver, by, selector, timeout=8):
    try:
        el = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        el.click()
        return True
    except (TimeoutException, NoSuchElementException):
        return False


def navegar_para_busca(driver):
    """
    Leva o driver até o formulário de busca do INPI.
    Trata CAPTCHA em qualquer ponto do fluxo.
    Retorna True se chegou ao formulário com sucesso.
    """
    driver.get(URL_INPI)
    time.sleep(2)
    verificar_e_resolver_captcha(driver)

    # Passo 1: "Continuar" (acesso sem autenticação)
    _clicar(driver, By.XPATH,
            "//input[contains(@value,'Continuar')] | //a[contains(text(),'Continuar')]")
    time.sleep(1)
    verificar_e_resolver_captcha(driver)

    # Passo 2: selecionar "Patente" se aparecer tela de seleção de tipo
    src = driver.page_source.lower()
    if "patente" in src and "modelo" in src:
        _clicar(driver, By.XPATH,
                "//a[normalize-space()='Patente'] | //td[contains(.,'Patente')]//a")
        time.sleep(1)
        verificar_e_resolver_captcha(driver)

    # Verifica se chegou ao formulário
    if _esperar(driver, By.NAME, "NumPedido", timeout=8):
        return True

    # Fallback: tenta acesso direto
    driver.get(URL_INPI)
    time.sleep(2)
    verificar_e_resolver_captcha(driver)
    return _esperar(driver, By.NAME, "NumPedido", timeout=8) is not None


def buscar_codigo(driver, codigo_busca):
    """Preenche o formulário e submete. Retorna True se encontrou resultados."""
    campo = _esperar(driver, By.NAME, "NumPedido", timeout=10)
    if not campo:
        raise Exception("Campo de busca não encontrado")

    campo.clear()
    campo.send_keys(codigo_busca)
    time.sleep(0.3)

    botao = _esperar(driver, By.XPATH,
                     "//input[@value='pesquisar »'] | //input[@type='submit']",
                     timeout=5)
    if botao:
        botao.click()
    else:
        campo.submit()

    time.sleep(2)
    verificar_e_resolver_captcha(driver)

    texto = driver.find_element(By.TAG_NAME, "body").text.lower()
    return not any(s in texto for s in [
        "não foram encontrados", "foram encontrados 0", "nenhum resultado"
    ])


def acessar_detalhe(driver):
    """Clica no primeiro resultado da lista. Retorna True se navegou para o detalhe."""
    try:
        link = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH,
                "//table//a[contains(@href,'PatenteServletController') or "
                "contains(@href,'Detalhe') or contains(@href,'detalhe')]"
            ))
        )
        link.click()
        time.sleep(1.5)
        verificar_e_resolver_captcha(driver)
        return True
    except TimeoutException:
        try:
            links = driver.find_elements(By.XPATH, "//table//tr[2]//a")
            if links:
                links[0].click()
                time.sleep(1.5)
                verificar_e_resolver_captcha(driver)
                return True
        except Exception:
            pass
        return False


# ─────────────────────────────────────────────────────────────
#  EXTRAÇÃO DE DADOS
# ─────────────────────────────────────────────────────────────

def _campo_tabela(soup, label):
    """
    Extrai valor de campo pelo label na tabela de detalhes do INPI.
    O INPI usa células como: | (71) Nome do Depositante: | Valor |
    Faz match exato primeiro, depois parcial como fallback.
    """
    label_lower = label.lower()

    # 1. Match exato (ignora prefixo numérico tipo "(71)")
    for td in soup.find_all("td"):
        texto = td.get_text(strip=True)
        # Remove prefixo numérico "(NN)" e dois-pontos do fim
        texto_limpo = re.sub(r'^\(\d+\)\s*', '', texto).rstrip(":").strip()
        if texto_limpo.lower() == label_lower:
            prox = td.find_next_sibling("td")
            if prox:
                return prox.get_text(" ", strip=True)

    # 2. Match parcial — garante que o label está contido mas não é apenas
    #    um substring de outra palavra (ex: "Titular" não deve casar "Depositante")
    for td in soup.find_all("td"):
        texto = td.get_text(strip=True).lower()
        if label_lower in texto:
            prox = td.find_next_sibling("td")
            if prox:
                val = prox.get_text(" ", strip=True)
                if val and val.lower() != label_lower:
                    return val
    return ""


def _limpar_nome(texto, limite=None):
    import unicodedata
    s = unicodedata.normalize('NFKD', str(texto)).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^A-Za-z0-9]', '', s)
    return s[:limite] if limite else s


def extrair_dados(driver, codigo_original):
    """Extrai todos os campos da página de detalhe — mesmo formato do Google Patents.

    Mapeamento INPI → planilha:
      Nome do Titular    → Current Assignee  (titular atual da patente)
      Nome do Procurador → Assignee          (representante legal)
      Nome do Inventor   → Inventores
      Nome do Depositante → campo auxiliar (usado se Titular não encontrado)
    """
    soup = BeautifulSoup(driver.page_source, "html.parser")

    num_pedido    = _campo_tabela(soup, "Nº do Pedido")
    titulo        = _campo_tabela(soup, "Título")
    resumo        = _campo_tabela(soup, "Resumo")
    inventor      = _campo_tabela(soup, "Nome do Inventor")
    ipc           = _campo_tabela(soup, "Classificação IPC")
    dt_deposito   = _campo_tabela(soup, "Data do Depósito")
    dt_publicacao = _campo_tabela(soup, "Data da Publicação")
    dt_concessao  = _campo_tabela(soup, "Data da Concessão")

    # ── Campos de titularidade ────────────────────────────────
    titular    = _campo_tabela(soup, "Nome do Titular")
    procurador = _campo_tabela(soup, "Nome do Procurador")
    depositante = _campo_tabela(soup, "Nome do Depositante")

    # Titular pode não existir em pedidos antigos — fallback para Depositante
    current_assignee = titular or depositante
    assignee         = procurador

    if dt_concessao in ("-", "- ", ""):
        dt_concessao = ""

    # Nome do arquivo usa o titular (ou depositante como fallback)
    pedido_limpo  = _limpar_nome(num_pedido or normalizar_codigo(codigo_original))
    tit_limpo     = _limpar_nome(current_assignee, limite=60)
    titulo_limpo  = _limpar_nome(titulo, limite=80)
    nome_arquivo  = f"{pedido_limpo}_{tit_limpo}_{titulo_limpo}"[:180]

    return {
        "Código":                 codigo_original,
        "Código Pesquisado":      num_pedido or normalizar_codigo(codigo_original),
        "Local":                  "BR",
        "Título":                 titulo,
        "Assignee":               assignee,
        "Inventores":             inventor,
        "Current Assignee":       current_assignee,
        "Filed Date":             dt_deposito,
        "First Publication Date": dt_publicacao,
        "Issue Date":             dt_concessao if dt_concessao else "X",
        "Abstract":               resumo if resumo else "Não contém resumo",
        "Nome do Arquivo":        nome_arquivo,
        "Assunto Primario":       ipc,
        "Assunto Secundario":     "",
        "Assunto Terciario":      "",
    }


def _data_vazia(codigo):
    return {c: "" for c in COLUNAS} | {
        "Código": codigo, "Local": "BR", "Issue Date": "X"
    }


# ─────────────────────────────────────────────────────────────
#  DOWNLOAD DE PDF — via JavaScript (único método que funciona)
# ─────────────────────────────────────────────────────────────

def tentar_download_pdf(driver, data):
    """
    Estratégia 1: execute_script no onclick do elemento salvaDocumento.
    Estratégia 2: clicar em links PDF na seção Documentos Publicados.
    Estratégia 3: requests com cookies da sessão para qualquer link .pdf.
    """
    os.makedirs(PASTA_PDF, exist_ok=True)
    nome = data.get("Nome do Arquivo", normalizar_codigo(data["Código"]))

    # ── Estratégia 1: salvaDocumento via JS ───────────────────
    try:
        elementos = driver.find_elements(
            By.XPATH,
            "//*[contains(@class,'salvaDocumento') or "
            "contains(@onclick,'salvaDocumento') or "
            "contains(@onclick,'download') or "
            "contains(@onclick,'Download')]"
        )
        for el in elementos:
            janelas_antes = set(driver.window_handles)
            pdfs_antes    = set(os.listdir(PASTA_PDF)) if os.path.exists(PASTA_PDF) else set()
            try:
                onclick = el.get_attribute("onclick") or ""
                if onclick:
                    driver.execute_script(onclick)
                else:
                    driver.execute_script("arguments[0].click();", el)
            except Exception:
                el.click()
            time.sleep(3)
            verificar_e_resolver_captcha(driver)

            # Verifica nova aba com PDF
            novas = set(driver.window_handles) - janelas_antes
            if novas:
                driver.switch_to.window(novas.pop())
                url_pdf = driver.current_url
                if ".pdf" in url_pdf.lower() or "pdf" in driver.page_source[:200].lower():
                    if _baixar_com_requests(url_pdf, nome, driver):
                        driver.close()
                        driver.switch_to.window(list(janelas_antes)[0])
                        return True
                driver.close()
                driver.switch_to.window(list(janelas_antes)[0])

            # Verifica download automático do Chrome
            if _aguardar_download(pdfs_antes, nome):
                return True
    except Exception:
        pass

    # ── Estratégia 2: links PDF em Documentos Publicados ──────
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for ancora in ["Documentos Publicados", "PDF", "Documento"]:
            tag = soup.find(string=re.compile(ancora, re.I))
            if tag:
                container = tag.find_parent("table") or tag.find_parent("tr")
                if container:
                    for a in container.find_all("a", href=True):
                        href = a["href"]
                        if "javascript" in href.lower():
                            continue
                        url = href if href.startswith("http") \
                              else "https://busca.inpi.gov.br" + href
                        if _baixar_com_requests(url, nome, driver):
                            return True
    except Exception:
        pass

    # ── Estratégia 3: qualquer link .pdf na página ────────────
    try:
        for link in driver.find_elements(
            By.XPATH, "//a[contains(translate(@href,'PDF','pdf'),'.pdf')]"
        ):
            href = link.get_attribute("href") or ""
            if "javascript" in href.lower():
                continue
            url = href if href.startswith("http") \
                  else "https://busca.inpi.gov.br" + href
            if _baixar_com_requests(url, nome, driver):
                return True
    except Exception:
        pass

    print(f"  PDF não disponível para {data['Código']}")
    return False


def _baixar_com_requests(url, nome, driver):
    """Baixa PDF usando requests com cookies do Selenium."""
    try:
        cookies = {c["name"]: c["value"] for c in driver.get_cookies()}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Referer": driver.current_url,
        }
        r = requests.get(url, cookies=cookies, headers=headers,
                         timeout=30, stream=True, verify=False)
        if r.status_code == 200 and "pdf" in r.headers.get("Content-Type", "").lower():
            caminho = os.path.join(PASTA_PDF, f"{nome}.pdf")
            with open(caminho, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
            print(f"  Download OK: {nome}.pdf")
            return True
    except Exception:
        pass
    return False


def _aguardar_download(pdfs_antes, nome, timeout=12):
    """Aguarda o Chrome terminar um download automático e renomeia o arquivo."""
    for _ in range(timeout * 2):
        if not os.path.exists(PASTA_PDF):
            time.sleep(0.5)
            continue
        arquivos  = set(os.listdir(PASTA_PDF))
        baixando  = [f for f in arquivos if f.endswith(".crdownload")]
        novos_pdf = [f for f in arquivos - pdfs_antes if f.endswith(".pdf")]
        if novos_pdf and not baixando:
            mais_recente = max(
                [os.path.join(PASTA_PDF, f) for f in novos_pdf],
                key=os.path.getmtime
            )
            destino = os.path.join(PASTA_PDF, f"{nome}.pdf")
            if mais_recente != destino and not os.path.exists(destino):
                shutil.move(mais_recente, destino)
            print(f"  Download OK: {nome}.pdf")
            return True
        time.sleep(0.5)
    return False


# ─────────────────────────────────────────────────────────────
#  SCRAPING COMPLETO DE UMA PATENTE
# ─────────────────────────────────────────────────────────────

def scrape_patente(driver, codigo_original):
    """
    Executa o fluxo completo para uma patente INPI:
    busca → resultado → detalhe → extração → download PDF.
    Retorna (data, found).
    Usado tanto pelo main() standalone quanto pelo main.py (opção 5).
    """
    codigo_busca = normalizar_codigo(codigo_original)
    print(f"  Buscando: {codigo_busca}...")

    if not navegar_para_busca(driver):
        raise Exception("Não foi possível chegar ao formulário de busca")

    if not buscar_codigo(driver, codigo_busca):
        print(f"  ✗ Não encontrado.")
        return _data_vazia(codigo_original), False

    if not acessar_detalhe(driver):
        print(f"  ✗ Não foi possível acessar o detalhe.")
        return _data_vazia(codigo_original), False

    data = extrair_dados(driver, codigo_original)

    if not data["Título"] and not data["Assignee"]:
        print(f"  ✗ Página sem dados úteis.")
        return _data_vazia(codigo_original), False

    print(f"  ✔ {data['Código Pesquisado']} — {data['Título'][:55]}...")

    if BAIXAR_PDFS:
        tentar_download_pdf(driver, data)

    return data, True


# ─────────────────────────────────────────────────────────────
#  EXCEL — usado apenas no modo standalone
# ─────────────────────────────────────────────────────────────

def salvar_excel(data_row, arquivo):
    df_new = pd.DataFrame([data_row])
    if not os.path.exists(arquivo):
        df_new.to_excel(arquivo, index=False, engine='openpyxl')
    else:
        df_ex = pd.read_excel(arquivo, engine='openpyxl')
        pd.concat([df_ex, df_new], ignore_index=True).to_excel(
            arquivo, index=False, engine='openpyxl'
        )


def salvar_revisao(data_row, motivo, arquivo=None):
    arquivo = arquivo or REVISAO_SAIDA
    row = dict(data_row)
    row["Status"] = motivo
    df_new = pd.DataFrame([row])
    if not os.path.exists(arquivo):
        df_new.to_excel(arquivo, index=False, engine='openpyxl')
    else:
        df_ex = pd.read_excel(arquivo, engine='openpyxl')
        if "Status" not in df_ex.columns:
            df_ex["Status"] = ""
        pd.concat([df_ex, df_new], ignore_index=True).to_excel(
            arquivo, index=False, engine='openpyxl'
        )
    wb = load_workbook(arquivo)
    ws = wb.active
    fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    for col in range(1, ws.max_column + 1):
        ws.cell(row=ws.max_row, column=col).fill = fill
    wb.save(arquivo)


def carregar_ja_processados():
    codigos = set()
    for arq in (EXCEL_SAIDA, REVISAO_SAIDA):
        if os.path.exists(arq):
            try:
                df = pd.read_excel(arq, engine='openpyxl')
                if "Código" in df.columns:
                    codigos.update(df["Código"].astype(str).str.strip().tolist())
            except Exception:
                pass
    return codigos


# ─────────────────────────────────────────────────────────────
#  MAIN — modo standalone
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  Catalogador INPI — modo standalone")
    print("=" * 55)
    print("\nAVISO: Chrome vai abrir em modo visível.")
    print("Se aparecer CAPTCHA, resolva e pressione ENTER no terminal.\n")

    os.makedirs(PASTA_PDF, exist_ok=True)
    ja_processados = carregar_ja_processados()
    total = len(CODIGOS_INPI)
    print(f"{total} código(s) na lista.\n")

    driver = setup_driver()
    ok = revisao = pulados = 0

    for i, codigo in enumerate(CODIGOS_INPI, start=1):
        codigo = codigo.strip()
        if not codigo:
            continue

        if codigo in ja_processados:
            print(f"[{i}/{total}] {codigo} — já processado. Pulando...")
            pulados += 1
            continue

        print(f"[{i}/{total}] {codigo}")

        tentativas = 0
        data = None
        found = False

        while tentativas < 3:
            try:
                data, found = scrape_patente(driver, codigo)
                break
            except WebDriverException as e:
                tentativas += 1
                print(f"  [AVISO] Driver travou. Reiniciando... ({tentativas}/3)")
                driver = reiniciar_driver(driver)
                time.sleep(2)
            except Exception as e:
                tentativas += 1
                print(f"  [AVISO] {e.__class__.__name__}: {e}. Tentativa {tentativas}/3...")
                time.sleep(2)
        else:
            print(f"  [ERRO] Falha após 3 tentativas.")
            salvar_revisao(_data_vazia(codigo), "Erro")
            revisao += 1
            continue

        if found:
            salvar_excel(data, EXCEL_SAIDA)
            ja_processados.add(codigo)
            ok += 1
        else:
            salvar_revisao(data, "Nao encontrado")
            ja_processados.add(codigo)
            revisao += 1

        time.sleep(1)

    try:
        driver.quit()
    except Exception:
        pass

    print("\n" + "=" * 55)
    print("Finalizado")
    print("=" * 55)
    print(f"  Encontrados: {ok}")
    print(f"  Revisão:     {revisao}")
    print(f"  Pulados:     {pulados}")
    if ok:     print(f"  Dados:  {EXCEL_SAIDA}")
    if revisao: print(f"  Revisão:{REVISAO_SAIDA}")
    if BAIXAR_PDFS: print(f"  PDFs:   {PASTA_PDF}/")


if __name__ == "__main__":
    main()
