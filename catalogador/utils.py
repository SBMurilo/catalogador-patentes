# ============================================================
#  utils.py — Funções Auxiliares
# ============================================================

import re


def extract_patent_code_from_filename(filename):
    """Extrai código da patente do nome do arquivo.
    Suporta prefixos de 2 ou 3 letras (ex: JPH, JPS)."""
    match = re.search(r'[A-Z]{2,3}\d+[A-Z]?\d*', filename.upper())
    return match.group(0) if match else None


def extract_country_code(patent_code):
    """Extrai o código do país do código da patente."""
    match = re.match(r"^([A-Z]{2})\d+", patent_code)
    return match.group(1) if match else "N/A"


def format_inventors(inventors_list):
    """Formata a lista de inventores para o padrão SOBRENOME, Nome."""
    formatted_names = []
    for name in inventors_list:
        parts = name.split()
        if len(parts) > 1:
            last_name = parts[-1].upper()
            first_name = " ".join(parts[:-1])
            formatted_names.append(f"{last_name}, {first_name}")
        else:
            formatted_names.append(name.upper())
    return ". ".join(formatted_names)


def gerar_nome_arquivo(data):
    """Gera o nome do arquivo no formato CódigoPesquisado_Assign_Titulo."""
    import unicodedata

    def _limpar(texto):
        sem_acento = unicodedata.normalize('NFKD', str(texto)).encode('ascii', 'ignore').decode('ascii')
        return re.sub(r'[^A-Za-z0-9]', '', sem_acento)

    numero   = data.get("Código Pesquisado") or data["Código"]
    assignee = _limpar(data["Assignee"])
    titulo   = _limpar(data["Título"])
    return f"{numero}_{assignee}_{titulo}"


def format_title_case(text):
    """Coloca a primeira letra de cada palavra em maiúscula."""
    if not text:
        return text
    return text.title()


def generate_patent_variations(patent_code):
    """Gera variações do código removendo zeros da parte numérica, um por vez."""
    match = re.match(r"([A-Z]{2})(0*\d+)([A-Z]\d*)", patent_code)
    if not match:
        return [patent_code]

    country, number, suffix = match.groups()
    variations = [patent_code]

    while number.startswith("0"):
        number = number[1:]
        variations.append(f"{country}{number}{suffix}")

    return variations


def generate_review_variations(code):
    """Gera variações adicionais para tentativa de correção.
    Suporta prefixos de 2 ou 3 letras (JPH, JPS, etc.)."""
    variations = []

    match = re.match(r"([A-Z]{2,3})(\d+)([A-Z]\d*)", code)
    if not match:
        return variations

    country, number, suffix = match.groups()

    # 1️⃣ adicionar zero na frente (EP532145A1 → EP0532145A1)
    if len(number) == 6:
        variations.append(f"{country}0{number}{suffix}")

    # 2️⃣ remover zero no meio — NUNCA nos primeiros 4 dígitos (protege o ano)
    #    Ex: EP5321045A1 → EP532145A1
    if "0" in number and len(number) >= 7:
        start = 4  # pula possível ano nos primeiros 4 dígitos
        for i in range(start, len(number) - 1):
            if number[i] == "0":
                new_number = number[:i] + number[i+1:]
                variations.append(f"{country}{new_number}{suffix}")
                break

    # 3️⃣ remover zeros da frente (EP00002345845A1 → EP2345845A1)
    match2 = re.match(r"([A-Z]{2,3})0+(\d+[A-Z]\d*)", code)
    if match2:
        variations.append(match2.group(1) + match2.group(2))

    # 4️⃣ adicionar zero depois do ano (US2009110579A1 → US20090110579A1)
    match3 = re.match(r"([A-Z]{2,3})(\d{4})(\d+)([A-Z]\d*)", code)
    if match3:
        c, year, num, suf = match3.groups()
        variations.append(f"{c}{year}0{num}{suf}")

    # 5️⃣ adicionar número final (AU84846816B → AU84846816B1)
    if re.match(r"[A-Z]{2,3}\d+[A-Z]$", code):
        variations.append(code + "1")

    # remover duplicados
    return list(dict.fromkeys(variations))
