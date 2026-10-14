# ============================================================
#  main.py — Menu Principal
# ============================================================

import os
import re
import sys
import shutil
import time

from selenium.common.exceptions import WebDriverException

from config import (EXCEL_FILE, REVIEW_FILE, TEST_PATENTS,
                    PASTA_INSERIR, PASTA_DESTINO, PASTA_SEM)
from scraper import setup_driver, get_patent_data, download_patent_pdf
from excel_manager import save_to_excel, save_to_review, load_processed_codes
from normalizer import extrair_codigo
from utils import generate_review_variations, gerar_nome_arquivo


# ── INPI — importação lazy (não exige dependências se não usar a opção 5)
def _importar_inpi():
    """Importa inpi_scraper.py em tempo de execução."""
    import importlib.util
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "inpi_scraper.py")
    if not os.path.exists(caminho):
        raise FileNotFoundError(
            f"inpi_scraper.py não encontrado em: {pasta}\n"
            "Coloque inpi_scraper.py na mesma pasta que main.py."
        )
    spec = importlib.util.spec_from_file_location("inpi_scraper", caminho)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _e_codigo_inpi(codigo):
    """Retorna True se parece ser código INPI brasileiro (PI, MU, C1...)."""
    return bool(re.match(
        r'^(PI|MU|C1|C2|C3|MI|BRPI|BRMU|RPI|MPI)\s*\d',
        codigo.strip().upper()
    ))


# ── Lista temporária de códigos INPI pendentes ───────────────
# Arquivo na mesma pasta do main.py
INPI_PENDENTES_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "inpi_pendentes.txt"
)


def _salvar_inpi_pendente(codigo):
    """Adiciona código à lista de pendentes INPI (sem duplicatas)."""
    existentes = _carregar_inpi_pendentes()
    if codigo not in existentes:
        with open(INPI_PENDENTES_FILE, "a", encoding="utf-8") as f:
            f.write(codigo + "\n")


def _carregar_inpi_pendentes():
    """Retorna lista de códigos pendentes do arquivo."""
    if not os.path.exists(INPI_PENDENTES_FILE):
        return []
    with open(INPI_PENDENTES_FILE, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]


def _remover_inpi_pendentes(codigos_remover):
    """Remove códigos da lista de pendentes (já processados ou já na planilha)."""
    if not os.path.exists(INPI_PENDENTES_FILE):
        return
    restantes = [c for c in _carregar_inpi_pendentes()
                 if c not in codigos_remover]
    with open(INPI_PENDENTES_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(restantes) + ("\n" if restantes else ""))


# Reinicia o driver a cada N patentes para evitar acúmulo de memória
_REINICIAR_A_CADA = 300


# ── Helpers de path / arquivo ────────────────────────────────

def _long_path(path):
    """Adiciona prefixo \\?\\ no Windows para suportar caminhos > 260 caracteres."""
    if sys.platform != "win32":
        return path
    path = os.path.abspath(path)
    if path.startswith("\\\\?\\"):
        return path
    if path.startswith("\\\\"):
        return "\\\\?\\UNC\\" + path[2:]
    return "\\\\?\\" + path


def _mover(origem, destino):
    shutil.move(_long_path(origem), _long_path(destino))


_MAX_NOME = 180


def _truncar_nome(nome):
    return nome[:_MAX_NOME] if len(nome) > _MAX_NOME else nome


def _destino_unico(pasta, nome_arquivo):
    """Garante nome único na pasta destino, adicionando _1, _2... se necessário."""
    destino = os.path.join(pasta, nome_arquivo)
    if not os.path.exists(_long_path(destino)):
        return destino
    base, ext = os.path.splitext(nome_arquivo)
    c = 1
    while True:
        novo = os.path.join(pasta, f"{base}_{c}{ext}")
        if not os.path.exists(_long_path(novo)):
            return novo
        c += 1


def _reiniciar_driver(driver):
    """Fecha o driver atual e abre um novo."""
    try:
        driver.quit()
    except Exception:
        pass
    print("\n  [Driver reiniciado]\n")
    return setup_driver()


# ── Núcleo: scraping + salvar no lugar certo ─────────────────

def _processar_patente(driver, codigo_original, pdf_path=None,
                       processed_codes=None, label=""):
    """
    Scraping de uma patente com salvamento automático no destino correto.

    pdf_path  : caminho do PDF já existente em disco (opção 3).
                None → tenta download do Google Patents (opções 1 e 2).
    label     : prefixo para o print, ex: "[12/200]"

    Fluxo:
      Encontrado + pdf_path        → renomeia PDF + move Patentes/ + planilha principal
      Encontrado + sem PDF + download OK  → baixa, renomeia, move Patentes/ + planilha principal
      Encontrado + sem PDF + sem download → planilha de revisão ("Download nao disponivel")
      Não encontrado + pdf_path    → PDF vai para Revisão/ + planilha de revisão
      Não encontrado + sem PDF     → planilha de revisão ("Nao encontrado")
      Erro driver 3x               → planilha de revisão ("Erro no driver")

    Retorna: (driver, resultado)
      resultado: 'ok' | 'sem_download' | 'nao_encontrado' | 'pulado' | 'erro'
    """
    pref = f"{label} " if label else "  "

    # ── Verificar se já foi processado ───────────────────────
    if processed_codes is not None:
        if codigo_original in processed_codes:
            print(f"{pref}{codigo_original} — já catalogado. Pulando...")
            return driver, 'pulado'
        from utils import generate_patent_variations
        todas = (generate_patent_variations(codigo_original)
                 + generate_review_variations(codigo_original))
        for v in todas:
            if v != codigo_original and v in processed_codes:
                print(f"{pref}{codigo_original} — já catalogado como {v}. Pulando...")
                return driver, 'pulado'

    # ── Código INPI? Salva na lista pendente e avisa ──────────
    if _e_codigo_inpi(codigo_original):
        _salvar_inpi_pendente(codigo_original)
        print(f"{pref}⚠  {codigo_original} → código INPI. "
              f"Salvo em pendentes — processe pela opção 5c.")
        return driver, 'inpi_pendente'

    print(f"{pref}Processando {codigo_original}...")

    # ── Scraping com reinício automático ─────────────────────
    tentativas = 0
    data = None
    data_extracted = False

    while tentativas < 3:
        try:
            data, data_extracted = get_patent_data(driver, codigo_original)

            if not data_extracted:
                for variacao in generate_review_variations(codigo_original):
                    print(f"  Tentando variação {variacao}...")
                    vdata, vfound = get_patent_data(driver, variacao)
                    if vfound:
                        data = vdata
                        data["Código"] = codigo_original
                        data["Código Pesquisado"] = variacao
                        data_extracted = True
                        print(f"  Encontrado com variação {variacao}")
                        break
            break

        except WebDriverException as e:
            tentativas += 1
            print(f"  [AVISO] Driver travou ({e.__class__.__name__}). "
                  f"Reiniciando... ({tentativas}/3)")
            driver = _reiniciar_driver(driver)
            time.sleep(2)
    else:
        # Falhou após 3 tentativas
        print(f"  [ERRO] Falha após 3 tentativas. Salvando na revisão.")
        data = {
            "Código": codigo_original, "Código Pesquisado": codigo_original,
            "Local": "", "Título": "", "Assignee": "", "Inventores": "",
            "Current Assignee": "", "Filed Date": "", "First Publication Date": "",
            "Issue Date": "", "Abstract": "", "Nome do Arquivo": "",
            "Assunto Primario": "", "Assunto Secundario": "", "Assunto Terciario": "",
        }
        save_to_review(data, REVIEW_FILE, status="Erro no driver")
        if pdf_path and os.path.exists(_long_path(pdf_path)):
            destino = _destino_unico(PASTA_SEM, f"{codigo_original}.pdf")
            _mover(pdf_path, destino)
        if processed_codes is not None:
            processed_codes.add(codigo_original)
        return driver, 'erro'

    # ── Não encontrado ────────────────────────────────────────
    if not data_extracted:
        save_to_review(data, REVIEW_FILE, status="Nao encontrado")
        if pdf_path and os.path.exists(_long_path(pdf_path)):
            destino = _destino_unico(PASTA_SEM, f"{codigo_original}.pdf")
            _mover(pdf_path, destino)
            print(f"  ✗ Não encontrado → Revisão/ (PDF movido)")
        else:
            print(f"  ✗ Não encontrado → Revisão")
        if processed_codes is not None:
            processed_codes.add(codigo_original)
        return driver, 'nao_encontrado'

    # ── Encontrado — preparar nome final ─────────────────────
    nome_arquivo = data.get("Nome do Arquivo", "")
    if not nome_arquivo or str(nome_arquivo).lower() in (
            "nan", "não aplicável", "nao aplicavel",
            "não é possível", "nao e possivel", ""):
        nome_arquivo = gerar_nome_arquivo(data)
    data["Nome do Arquivo"] = nome_arquivo
    nome_base = _truncar_nome(nome_arquivo)

    # ── Opção 3: PDF já existe → renomeia e move para Patentes/ ──
    if pdf_path:
        novo_nome = nome_base + ".pdf"
        destino = _destino_unico(PASTA_DESTINO, novo_nome)
        _mover(pdf_path, destino)
        data["Nome do Arquivo"] = os.path.splitext(os.path.basename(destino))[0]
        save_to_excel(data, EXCEL_FILE, False)
        print(f"  ✔ {codigo_original} → Patentes/{os.path.basename(destino)}")
        if processed_codes is not None:
            processed_codes.add(codigo_original)
        return driver, 'ok'

    # ── Opções 1/2: tenta download ───────────────────────────
    codigo_pesquisado = data.get("Código Pesquisado", codigo_original)
    baixou = download_patent_pdf(driver, codigo_pesquisado, PASTA_DESTINO)

    if baixou:
        # Renomeia o PDF baixado de {codigo_pesquisado}.pdf para o nome final
        baixado = os.path.join(PASTA_DESTINO, f"{codigo_pesquisado}.pdf")
        novo_nome = nome_base + ".pdf"
        destino = _destino_unico(PASTA_DESTINO, novo_nome)
        if os.path.exists(_long_path(baixado)):
            _mover(baixado, destino)
        data["Nome do Arquivo"] = os.path.splitext(os.path.basename(destino))[0]
        save_to_excel(data, EXCEL_FILE, False)
        print(f"  ✔ {codigo_original} → Patentes/{os.path.basename(destino)} "
              f"+ planilha principal")
        if processed_codes is not None:
            processed_codes.add(codigo_original)
        return driver, 'ok'

    else:
        save_to_review(data, REVIEW_FILE, status="Download nao disponivel")
        print(f"  ~ {codigo_original} → Revisão (sem download, dados salvos)")
        if processed_codes is not None:
            processed_codes.add(codigo_original)
        return driver, 'sem_download'


# ── Opção 1: Adicionar patente manualmente ───────────────────

def run_adicionar_manual(driver, processed_codes):
    """
    Usuário digita um código. O programa faz scraping e:
    - Achou + tem download   → PDF em Patentes/ + planilha principal
    - Achou + sem download   → planilha de revisão ("Download nao disponivel")
    - Não achou              → planilha de revisão ("Nao encontrado")
    """
    while True:
        code = input("\nDigite o código da patente (ou 'sair'): ").strip().upper()
        if code == "SAIR":
            break
        if not code:
            continue
        if not re.match(r'^[A-Z]{2,3}[A-Z0-9]{3,}$', code):
            print("  Código inválido. Use o formato correto "
                  "(ex: US9023456B2, JPH077859A, BR102021012613A2).")
            continue
        try:
            driver, _ = _processar_patente(
                driver, code, processed_codes=processed_codes
            )
        except WebDriverException:
            print("  [AVISO] Driver travou. Reiniciando...")
            driver = _reiniciar_driver(driver)
    return driver


# ── Opção 2: Processar lista de teste ────────────────────────

def run_lista_teste(driver, processed_codes):
    """
    Processa a lista TEST_PATENTS de config.py.
    Para cada código:
    - Achou + tem download   → PDF em Patentes/ + planilha principal
    - Achou + sem download   → planilha de revisão ("Download nao disponivel")
    - Não achou              → planilha de revisão ("Nao encontrado")
    """
    total = len(TEST_PATENTS)
    print(f"\nProcessando {total} patentes da lista de teste...\n")

    desde_reinicio = 0
    contadores = {'ok': 0, 'sem_download': 0, 'nao_encontrado': 0,
                  'pulado': 0, 'erro': 0, 'inpi_pendente': 0}
    start_time = time.time()

    for i, code in enumerate(TEST_PATENTS, start=1):
        if desde_reinicio >= _REINICIAR_A_CADA:
            print(f"  [Reinício preventivo após {_REINICIAR_A_CADA} patentes]")
            driver = _reiniciar_driver(driver)
            desde_reinicio = 0
        try:
            driver, resultado = _processar_patente(
                driver, code,
                processed_codes=processed_codes,
                label=f"[{i}/{total}]"
            )
            contadores[resultado] = contadores.get(resultado, 0) + 1
            if resultado != 'pulado':
                desde_reinicio += 1
        except WebDriverException:
            print("  [AVISO] Driver travou. Reiniciando...")
            driver = _reiniciar_driver(driver)
            desde_reinicio = 0

    elapsed = time.time() - start_time
    processados = sum(v for k, v in contadores.items() if k != 'pulado')
    medio = elapsed / processados if processados > 0 else 0

    print("\nLista de teste finalizada.")
    print(f"  OK (com PDF):       {contadores.get('ok', 0)}")
    print(f"  Sem download:       {contadores.get('sem_download', 0)}")
    print(f"  Não encontrados:    {contadores.get('nao_encontrado', 0)}")
    print(f"  Pulados:            {contadores.get('pulado', 0)}")
    if contadores.get('inpi_pendente', 0):
        print(f"  ⚠  INPI pendentes:  {contadores['inpi_pendente']}  "
              f"→ processe pela opção 5c")
    if contadores.get('erro', 0):
        print(f"  Erros:              {contadores['erro']}")
    print(f"  Tempo total: {elapsed:.0f}s | Médio por patente: {medio:.1f}s")

    return driver


# ── Opção 3: Catalogar PDFs da pasta Inserir/ ────────────────

def run_catalogar_pdfs(driver, processed_codes):
    """
    Para cada PDF em Inserir/ (incluindo subpastas):
      1. Extrai o código do nome do arquivo
      2. Faz scraping no Google Patents
      3. Achou  → renomeia PDF + move para Patentes/ + planilha principal
      4. Não achou → PDF vai para Revisão/ + planilha de revisão
      5. Sem código → move para Revisão/ sem processar

    Reinicia o driver automaticamente a cada _REINICIAR_A_CADA patentes.
    """
    if not os.path.exists(_long_path(PASTA_INSERIR)):
        print(f"ERRO: Pasta Inserir não encontrada: {PASTA_INSERIR}")
        print("Verifique o caminho em config.py.")
        return driver

    # Coleta todos os PDFs recursivamente
    arquivos_caminhos = []
    for raiz, _, files in os.walk(_long_path(PASTA_INSERIR)):
        for f in files:
            if f.lower().endswith(".pdf"):
                arquivos_caminhos.append(os.path.join(raiz, f))

    total = len(arquivos_caminhos)
    if not total:
        print("Nenhum PDF encontrado em Inserir/.")
        return driver

    print(f"\n{total} PDF(s) encontrado(s) em Inserir/...\n")
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    os.makedirs(PASTA_SEM, exist_ok=True)

    desde_reinicio = 0
    contadores = {'ok': 0, 'sem_download': 0, 'nao_encontrado': 0,
                  'pulado': 0, 'sem_codigo': 0, 'erro': 0, 'inpi_pendente': 0}
    start_time = time.time()

    for i, caminho in enumerate(arquivos_caminhos, start=1):
        arquivo = os.path.basename(caminho)
        codigo = extrair_codigo(arquivo)

        if not codigo:
            # Sem código reconhecível → move para Revisão/
            destino = _destino_unico(PASTA_SEM, arquivo)
            _mover(caminho, destino)
            print(f"[{i}/{total}] [SEM CÓDIGO] {arquivo} → Revisão/")
            contadores['sem_codigo'] += 1
            continue

        codigo = codigo.upper()

        # Reinício preventivo a cada N patentes
        if desde_reinicio >= _REINICIAR_A_CADA:
            print(f"  [Reinício preventivo após {_REINICIAR_A_CADA} patentes]")
            driver = _reiniciar_driver(driver)
            desde_reinicio = 0

        try:
            driver, resultado = _processar_patente(
                driver, codigo,
                pdf_path=caminho,
                processed_codes=processed_codes,
                label=f"[{i}/{total}]"
            )
            contadores[resultado] = contadores.get(resultado, 0) + 1
            if resultado != 'pulado':
                desde_reinicio += 1
        except WebDriverException:
            print(f"  [AVISO] Driver travou. Reiniciando...")
            driver = _reiniciar_driver(driver)
            desde_reinicio = 0

    elapsed = time.time() - start_time
    processados = sum(v for k, v in contadores.items() if k != 'pulado')
    medio = elapsed / processados if processados > 0 else 0

    print("\n============================")
    print("Catalogação finalizada")
    print("============================")
    print(f"  Organizados em Patentes/:  {contadores['ok']}")
    print(f"  Sem download (revisão):    {contadores['sem_download']}")
    print(f"  Não encontrados (revisão): {contadores['nao_encontrado']}")
    print(f"  Sem código (revisão):      {contadores['sem_codigo']}")
    print(f"  Pulados (já existentes):   {contadores['pulado']}")
    if contadores.get('inpi_pendente', 0):
        print(f"  ⚠  INPI pendentes:         {contadores['inpi_pendente']}  "
              f"→ processe pela opção 5c")
    if contadores.get('erro', 0):
        print(f"  Erros:                     {contadores['erro']}")
    print(f"  Tempo total: {elapsed:.0f}s | Médio por patente: {medio:.1f}s")

    return driver


# ── Opção 4: Verificador de consistência ─────────────────────

def run_verificador():
    """
    Compara 'Nome do Arquivo' da planilha principal com arquivos físicos
    em Patentes/ e reporta o que está faltando.
    """
    import pandas as pd

    print("\n--- Verificador de consistência ---\n")

    if not os.path.exists(EXCEL_FILE):
        print(f"ERRO: Planilha não encontrada: {EXCEL_FILE}")
        return

    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')

    if "Nome do Arquivo" not in df.columns:
        print("ERRO: Coluna 'Nome do Arquivo' não encontrada na planilha.")
        return

    # Arquivos físicos em Patentes/ (sem extensão, uppercase para comparação)
    if os.path.exists(PASTA_DESTINO):
        arquivos_fisicos = {
            os.path.splitext(f)[0].upper()
            for f in os.listdir(PASTA_DESTINO)
            if f.lower().endswith(".pdf")
        }
    else:
        arquivos_fisicos = set()

    total_planilha = len(df)
    faltando = []
    sem_nome = []
    ok = 0

    for _, row in df.iterrows():
        nome = str(row.get("Nome do Arquivo", "")).strip()
        codigo = str(row.get("Código", "")).strip()

        if not nome or nome.lower() in ("nan", "não é possível", "nao e possivel",
                                        "não aplicável", "nao aplicavel",
                                        "não aplicavel"):
            sem_nome.append(codigo)
            continue

        if nome.upper() in arquivos_fisicos:
            ok += 1
        else:
            faltando.append((codigo, nome))

    # --- Relatório ---
    print(f"  Total na planilha:          {total_planilha}")
    print(f"  Encontrados em Patentes/:   {ok}")
    print(f"  Sem nome de arquivo:        {len(sem_nome)}  "
          f"(download indisponível ou não processado)")
    print(f"  FALTANDO em Patentes/:      {len(faltando)}")

    if sem_nome:
        print(f"\n  Códigos sem nome de arquivo ({len(sem_nome)}):")
        for c in sem_nome:
            print(f"    - {c}")

    if faltando:
        print(f"\n  Faltando em Patentes/ ({len(faltando)}):")
        for codigo, nome in faltando:
            print(f"    [{codigo}]  {nome}.pdf")

        relatorio = "faltando_patentes.txt"
        with open(relatorio, "w", encoding="utf-8") as f:
            f.write(f"Faltando em Patentes/ — {len(faltando)} arquivo(s)\n")
            f.write("=" * 60 + "\n\n")
            for codigo, nome in faltando:
                f.write(f"[{codigo}]  {nome}.pdf\n")
        print(f"\n  Relatório salvo em: {relatorio}")
    else:
        print("\n  Tudo certo! Todos os arquivos esperados estão em Patentes/.")


# ── Opção 5: Patentes INPI brasileiras ───────────────────────

def run_inpi(processed_codes):
    """
    Opção 5 — Catalogar patentes INPI (PI, MU, C1...).
      a - Digitar código(s) manualmente
      b - Usar lista CODIGOS_INPI do inpi_scraper.py
      c - Processar lista de pendentes (detectados automaticamente nas opções 1/2/3)
    Salva resultados no mesmo EXCEL_FILE e REVIEW_FILE do sistema principal.
    PDFs vão para PASTA_DESTINO (Patentes/).
    """
    try:
        inpi = _importar_inpi()
    except FileNotFoundError as e:
        print(f"\n  ERRO: {e}")
        return

    # ── Mostra quantos pendentes existem ─────────────────────
    pendentes = _carregar_inpi_pendentes()
    pendentes_novos = [c for c in pendentes if c not in processed_codes]
    aviso_pendentes = (f"  ({len(pendentes_novos)} pendente(s) da fila automática)"
                       if pendentes_novos else "")

    print("\n  Como deseja informar os códigos?")
    print("  a - Digitar código(s) agora")
    print("  b - Usar lista CODIGOS_INPI do inpi_scraper.py")
    print(f"  c - Processar fila automática (opções 1/2/3){aviso_pendentes}")
    sub = input("\n  Escolha (a / b / c): ").strip().lower()

    if sub == "a":
        print("\n  Digite os códigos separados por vírgula ou um por linha.")
        print("  Linha em branco para terminar.\n")
        codigos = []
        while True:
            linha = input("  Código(s): ").strip()
            if not linha:
                break
            partes = re.split(r'[,;\n]+', linha)
            codigos.extend(p.strip() for p in partes if p.strip())
        if not codigos:
            print("  Nenhum código informado.")
            return

    elif sub == "b":
        codigos = list(inpi.CODIGOS_INPI)
        print(f"\n  {len(codigos)} código(s) encontrado(s) em inpi_scraper.py.")

    elif sub == "c":
        # Carrega pendentes e limpa os que já estão na planilha
        todos_pendentes = _carregar_inpi_pendentes()
        ja_na_planilha  = [c for c in todos_pendentes if c in processed_codes]
        codigos         = [c for c in todos_pendentes if c not in processed_codes]

        if ja_na_planilha:
            print(f"\n  {len(ja_na_planilha)} código(s) já na planilha — removendo da fila:")
            for c in ja_na_planilha:
                print(f"    - {c}")
            _remover_inpi_pendentes(set(ja_na_planilha))

        if not codigos:
            print("\n  Fila vazia. Nada para processar.")
            return
        print(f"\n  {len(codigos)} código(s) na fila para processar.")

    else:
        print("  Sub-opção inválida.")
        return

    # ── Filtra já processados ─────────────────────────────────
    codigos_novos = [c for c in codigos if c.strip() not in processed_codes]
    pulados = len(codigos) - len(codigos_novos)
    if pulados:
        print(f"  {pulados} já processado(s). Pulando...")
    if not codigos_novos:
        print("  Nada novo para processar.")
        if sub == "c":
            _remover_inpi_pendentes(set(codigos))
        return

    print(f"\n  {len(codigos_novos)} código(s) a processar.")
    print("  AVISO: Chrome vai abrir em modo visível.")
    print("  Se aparecer CAPTCHA, resolva e pressione ENTER no terminal.\n")

    os.makedirs(inpi.PASTA_PDF, exist_ok=True)
    os.makedirs(PASTA_DESTINO, exist_ok=True)

    driver_inpi = inpi.setup_driver()
    total = len(codigos_novos)
    ok = revisao = erros = 0
    processados_agora = set()

    for i, codigo in enumerate(codigos_novos, start=1):
        codigo = codigo.strip()
        if not codigo:
            continue

        print(f"[{i}/{total}] {codigo}")

        tentativas = 0
        data = None
        found = False

        while tentativas < 3:
            try:
                data, found = inpi.scrape_patente(driver_inpi, codigo)
                break
            except Exception as e:
                tentativas += 1
                print(f"  [AVISO] {e.__class__.__name__}. Tentativa {tentativas}/3...")
                driver_inpi = inpi.reiniciar_driver(driver_inpi)
                time.sleep(2)
        else:
            print(f"  [ERRO] Falha após 3 tentativas.")
            save_to_review(inpi._data_vazia(codigo), REVIEW_FILE, status="Erro INPI")
            processados_agora.add(codigo)
            erros += 1
            continue

        if found:
            nome_base = data.get("Nome do Arquivo", "")
            pdf_origem = os.path.join(inpi.PASTA_PDF, f"{nome_base}.pdf")
            if os.path.exists(pdf_origem):
                destino = _destino_unico(PASTA_DESTINO, f"{nome_base}.pdf")
                _mover(pdf_origem, destino)
                data["Nome do Arquivo"] = os.path.splitext(os.path.basename(destino))[0]
                print(f"  ✔ PDF → Patentes/{os.path.basename(destino)}")
            save_to_excel(data, EXCEL_FILE, False)
            processed_codes.add(codigo)
            processados_agora.add(codigo)
            ok += 1
        else:
            save_to_review(data, REVIEW_FILE, status="Nao encontrado INPI")
            processed_codes.add(codigo)
            processados_agora.add(codigo)
            revisao += 1

        # Remove da fila imediatamente após processar — garante que se o programa
        # for interrompido no meio, os já processados não aparecem de novo na fila.
        _remover_inpi_pendentes({codigo})

        time.sleep(0.5)

    try:
        driver_inpi.quit()
    except Exception:
        pass

    # processados_agora mantido para o relatório final (não é mais necessário para remoção)
    print("\n============================")
    print("INPI finalizado")
    print("============================")
    print(f"  Encontrados:  {ok}")
    print(f"  Revisão:      {revisao}")
    if erros:
        print(f"  Erros:        {erros}")
    restantes = len(_carregar_inpi_pendentes())
    if restantes:
        print(f"\n  ⚠  Ainda há {restantes} código(s) na fila → opção 5c")


# ── Menu ─────────────────────────────────────────────────────

def exibir_menu():
    pendentes = len(_carregar_inpi_pendentes())
    aviso = f"  ⚠  ({pendentes} na fila)" if pendentes else ""
    print("\n========================================")
    print("       Catalogador de Patentes")
    print("========================================")
    print("  1 - Adicionar patente manualmente")
    print("  2 - Processar lista de teste")
    print("  3 - Catalogar PDFs da pasta Inserir")
    print("  4 - Verificar consistência planilha vs Patentes/")
    print(f"  5 - Catalogar patentes INPI (PI, MU, C1...){aviso}")
    print("  0 - Sair")
    print("========================================")


def main():
    while True:
        processed_codes = load_processed_codes(EXCEL_FILE, REVIEW_FILE)
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nEncerrando. Até logo!")
            break

        elif opcao == "4":
            run_verificador()

        elif opcao == "5":
            run_inpi(processed_codes)

        elif opcao in ("1", "2", "3"):
            driver = setup_driver()
            try:
                if opcao == "1":
                    driver = run_adicionar_manual(driver, processed_codes)
                elif opcao == "2":
                    driver = run_lista_teste(driver, processed_codes)
                elif opcao == "3":
                    driver = run_catalogar_pdfs(driver, processed_codes)
            finally:
                try:
                    driver.quit()
                except Exception:
                    pass

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()
