# ============================================================
#  scraper.py — Configuração do Driver e Extração de Dados
# ============================================================

import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from utils import (
    extract_country_code,
    format_title_case,
    format_inventors,
    gerar_nome_arquivo,
    generate_patent_variations,
)


def setup_driver():
    """Configura e retorna o WebDriver do Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--blink-settings=imagesEnabled=false")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)  # Timeout de carregamento de página
    return driver


# ── Funções de Extração de Dados Específicas ─────────────────

def extract_title_and_abstract(driver, data):
    try:
        data["Título"] = driver.find_element(By.CSS_SELECTOR, "h1#title").text.strip()
    except NoSuchElementException:
        pass
    try:
        abstract_element = driver.find_element(By.CSS_SELECTOR, "section#abstract")
        data["Abstract"] = abstract_element.text.replace("Abstract", "").strip()
    except NoSuchElementException:
        pass


def extract_inventors(driver, data):
    inventors = [
        e.text.strip()
        for e in driver.find_elements(
            By.CSS_SELECTOR, "dd[itemprop='inventor'] span[itemprop='name']"
        )
        if e.text.strip()
    ]
    if not inventors:
        try:
            dd = driver.find_element(
                By.XPATH, "//dt[contains(text(),'Inventor')]/following-sibling::dd[1]"
            )
            texto = dd.text.strip()
            inventors = re.split(r",| and ", texto)
            inventors = [i.strip() for i in inventors if i.strip()]
        except NoSuchElementException:
            pass
    inventors = list(dict.fromkeys(inventors))
    data["Inventores"] = format_inventors(inventors)


def extract_assignees(driver, page_text, data):
    try:
        data["Assignee"] = driver.find_element(
            By.XPATH,
            "//dt[contains(text(), 'Applicant')]/following-sibling::dd[1]/span[@itemprop='name']"
        ).text.strip()
    except NoSuchElementException:
        try:
            data["Assignee"] = driver.find_element(
                By.XPATH,
                "//dt[contains(text(), 'Assignee')]/following-sibling::dd[1]/span[@itemprop='name']"
            ).text.strip()
        except NoSuchElementException:
            pass
    try:
        current_assignee_element = driver.find_element(
            By.XPATH,
            "//dt[contains(text(), 'Current Assignee')]/following-sibling::dd[1]"
        )
        data["Current Assignee"] = current_assignee_element.text.strip()
    except NoSuchElementException:
        match_current_assignee = re.search(r"Current Assignee\s*\n\s*([^\n]+)", page_text)
        if match_current_assignee:
            data["Current Assignee"] = match_current_assignee.group(1).strip()
    if not data["Assignee"]:
        match_filed_by = re.search(r"Application filed by\s+([^\n]+)", page_text)
        if match_filed_by:
            data["Assignee"] = match_filed_by.group(1).strip()


def extract_dates(driver, page_text, data):
    dates = {"Filed": "", "Publication": [], "Granted": ""}
    page_text_lower = page_text.lower()

    dt_elements = driver.find_elements(By.TAG_NAME, "dt")
    for dt in dt_elements:
        dt_text = dt.text.strip().lower()
        try:
            dd_element = dt.find_element(By.XPATH, ".//following-sibling::dd[1]")
            dd_text = dd_element.text.strip()
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', dd_text)
            if date_match:
                date_val = date_match.group(1)
                if "filed" in dt_text and not dates["Filed"]:
                    dates["Filed"] = date_val
                if "publication" in dt_text:
                    dates["Publication"].append(date_val)
                if ("granted" in dt_text or "issue" in dt_text) and not dates["Granted"]:
                    dates["Granted"] = date_val
        except NoSuchElementException:
            continue

    page_text_lines = page_text.split("\n")
    for line in page_text_lines:
        line_clean = line.strip()
        date_match = re.search(r'^(\d{4}-\d{2}-\d{2})', line_clean)
        if date_match:
            date_val = date_match.group(1)
            context = line_clean.lower()
            try:
                next_line_index = page_text_lines.index(line) + 1
                if next_line_index < len(page_text_lines):
                    context += " " + page_text_lines[next_line_index].lower()
            except:
                pass
            if "filed" in context and not dates["Filed"]:
                dates["Filed"] = date_val
            if "publication" in context:
                dates["Publication"].append(date_val)
            if "application granted" in context and not dates["Granted"]:
                dates["Granted"] = date_val

    if not dates["Filed"]:
        match_filed = re.search(r"filed(?: date)?\s*[:]?\s*(\d{4}-\d{2}-\d{2})", page_text_lower)
        if match_filed:
            dates["Filed"] = match_filed.group(1)
    if not dates["Publication"]:
        match_pub = re.findall(r"publication(?: date)?\s*[:]?\s*(\d{4}-\d{2}-\d{2})", page_text_lower)
        if match_pub:
            dates["Publication"].extend(match_pub)
    if not dates["Granted"]:
        match_granted_line = re.search(r"(\d{4}-\d{2}-\d{2})\s*(?:•\s*)?Application granted", page_text)
        if match_granted_line:
            dates["Granted"] = match_granted_line.group(1)

    data["Filed Date"]             = dates["Filed"]
    data["First Publication Date"] = sorted(dates["Publication"])[0] if dates["Publication"] else ""
    data["Issue Date"]             = dates["Granted"] if dates["Granted"] else "X"


# ── Função Principal de Extração ─────────────────────────────

def get_patent_data(driver, patent_code):
    """
    Navega até a página da patente e extrai as informações.
    Lança WebDriverException se o driver travar (para ser capturado em main.py).
    """
    original_code  = patent_code
    variations     = generate_patent_variations(patent_code)
    title_elements = []

    for code in variations:
        url = f"https://patents.google.com/patent/{code}/en?oq={code}"
        # WebDriverException propaga — main.py vai reiniciar o driver
        driver.get(url)
        time.sleep(0.8)
        title_elements = driver.find_elements(By.CSS_SELECTOR, "h1#title")
        if title_elements:
            canonical_match = re.search(r'/patent/([^/]+)/', driver.current_url)
            patent_code = canonical_match.group(1) if canonical_match else code
            break

    if not title_elements:
        print(f"{patent_code} não encontrado no Google Patents.")
        return {
            "Código":                original_code,
            "Código Pesquisado":     patent_code,
            "Local":                 extract_country_code(patent_code),
            "Título":                "Não encontrado",
            "Assignee":              "",
            "Inventores":            "",
            "Current Assignee":      "",
            "Filed Date":            "",
            "First Publication Date": "",
            "Issue Date":            "",
            "Abstract":              "",
            "Nome do Arquivo":       "Não é Possível",
            "Assunto Primario":      "",
            "Assunto Secundario":    "",
            "Assunto Terciario":     "",
        }, False

    WebDriverWait(driver, 4).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    data = {
        "Código":                original_code,
        "Código Pesquisado":     patent_code,
        "Local":                 extract_country_code(patent_code),
        "Título":                "",
        "Assignee":              "",
        "Inventores":            "",
        "Current Assignee":      "",
        "Filed Date":            "",
        "First Publication Date": "",
        "Issue Date":            "",
        "Abstract":              "",
        "Nome do Arquivo":       "Não aplicável",
        "Assunto Primario":      "",
        "Assunto Secundario":    "",
        "Assunto Terciario":     "",
    }
    data_extracted = False

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1#title")))
        page_text = driver.find_element(By.TAG_NAME, "body").text

        extract_title_and_abstract(driver, data)
        extract_inventors(driver, data)
        extract_assignees(driver, page_text, data)
        extract_dates(driver, page_text, data)

        data["Título"]           = format_title_case(data["Título"])
        data["Assignee"]         = format_title_case(data["Assignee"])
        data["Current Assignee"] = format_title_case(data["Current Assignee"])
        data["Abstract"]         = re.sub(
            r"translated from [A-Za-z]+", "", data["Abstract"], flags=re.IGNORECASE
        ).strip()

        inventor = data["Inventores"].split(".")[0].strip()
        assignee = data["Assignee"]
        if data["Assignee"].lower() == "individual":
            data["Assignee"] = inventor
        if data["Current Assignee"].lower() == "individual":
            data["Current Assignee"] = inventor
        if not data["Current Assignee"].strip():
            data["Current Assignee"] = assignee
        if not data["Abstract"].strip():
            data["Abstract"] = "Não contém resumo"

        data["Nome do Arquivo"] = gerar_nome_arquivo(data)
        data_extracted = True

    except TimeoutException:
        print(f"Erro: Tempo limite excedido ao carregar a página para {patent_code}.")
        data["Título"]          = "Não Encontrado"
        data["Nome do Arquivo"] = "Não é Possível"
        data_extracted = False

    except WebDriverException:
        raise  # Propaga para main.py reiniciar o driver

    except Exception as e:
        print(f"Erro inesperado ao processar {patent_code}: {e}")
        data_extracted = False

    return data, data_extracted


# ── Download de PDF ──────────────────────────────────────────

def download_patent_pdf(driver, patent_code, pasta_destino):
    import requests
    import os

    pdf_url = None
    try:
        links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
        for link in links:
            href = link.get_attribute("href")
            if href and "patentimages.storage.googleapis.com" in href:
                pdf_url = href
                break
    except Exception:
        pass

    if not pdf_url:
        pdf_url = f"https://patentimages.storage.googleapis.com/pdfs/{patent_code}.pdf"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(pdf_url, headers=headers, timeout=30, stream=True)
        if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
            os.makedirs(pasta_destino, exist_ok=True)
            caminho = os.path.join(pasta_destino, f"{patent_code}.pdf")
            with open(caminho, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"  Download OK: {patent_code}.pdf")
            return True
        else:
            print(f"  Download falhou ({response.status_code}): {patent_code}")
            return False
    except Exception as e:
        print(f"  Download falhou (erro): {patent_code} — {e}")
        return False
