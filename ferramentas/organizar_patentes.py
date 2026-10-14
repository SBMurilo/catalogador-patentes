"""
organizar_patentes.py
─────────────────────
Automação de classificação e organização de patentes.

Uso:
    python organizar_patentes.py

O script exibe um menu interativo no terminal com as opções disponíveis.
Nenhum argumento de linha de comando é necessário.
"""

import os
import re
import sys
import shutil
import pathlib
from collections import defaultdict
from datetime import datetime

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ══════════════════════════════════════════════════════════════════════
# CONFIGURACAO — ajuste os caminhos conforme seu ambiente
# ══════════════════════════════════════════════════════════════════════

EXCEL_FILE    = r"C:\Projetos\Testes_Prog_Patente\Projeto\patents_data_test.xlsx"
PASTA_PDFS    = r"C:\Projetos\Testes_Prog_Patente\Projeto\Patentes"
PASTA_DESTINO = r"C:\Projetos\Testes_Prog_Patente\Projeto\patents_organized"
RELATORIO     = r"C:\Projetos\Testes_Prog_Patente\Projeto\relatorio_organizacao.xlsx"

SCORE_MINIMO  = 2

# ══════════════════════════════════════════════════════════════════════
# CARREGA PALAVRAS-CHAVE
# ══════════════════════════════════════════════════════════════════════

SCRIPT_DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from palavras_chave import PALAVRAS_CHAVE
except ImportError:
    print(f"\n  X palavras_chave.py nao encontrado em: {SCRIPT_DIR}")
    print("  Coloque palavras_chave.py na mesma pasta deste script.\n")
    raise SystemExit(1)

# Pre-compila padroes + pesos
_COMPILED: dict = {}
for _pasta, _palavras in PALAVRAS_CHAVE.items():
    _COMPILED[_pasta] = [
        (_t, re.compile(re.escape(_t.lower())),
         3 if len(_t.split()) >= 3 else (2 if len(_t.split()) == 2 else 1))
        for _t in _palavras
    ]

_CB        = " (Confianca Baixa/Abstract Curto)"
_SEM_CLASS = "Sem_Classificacao"


# ══════════════════════════════════════════════════════════════════════
# MOTOR DE CLASSIFICACAO
# ══════════════════════════════════════════════════════════════════════

def _calcular_scores(texto: str, limiar: int = None) -> dict:
    lim = limiar if limiar is not None else SCORE_MINIMO
    t   = texto.lower()
    return {
        p: s for p, entradas in _COMPILED.items()
        if (s := sum(w for _, pat, w in entradas if pat.search(t))) >= lim
    }


def _filtro_hierarquico(scores: dict) -> dict:
    f, ks = dict(scores), set(scores)
    for p in list(f):
        if any(o.startswith(p + "/") for o in ks if o != p):
            f.pop(p, None)
    return f or scores


def _fallback_score1(texto: str):
    sub = {p: s for p, s in _calcular_scores(texto, 1).items() if "/" in p}
    if not sub:
        return None
    filt = _filtro_hierarquico(sub)
    ords = sorted(filt.items(), key=lambda kv: (-kv[0].count("/"), -kv[1]))
    d    = [p + _CB for p, _ in ords]
    return (d[0] if d else ""), (d[1] if len(d) > 1 else ""), \
           (d[2] if len(d) > 2 else ""), len(d), "Classificada (Confianca Baixa)"


def _classificar_por_texto(texto: str) -> tuple:
    """
    Tenta classificar um bloco de texto usando o fluxo padrão.
    Retorna (p1, p2, p3, n, status) ou None se nenhum match.
    """
    scores = _calcular_scores(texto)
    if not scores:
        return None

    filt = _filtro_hierarquico(scores)
    ords = sorted(filt.items(), key=lambda kv: (-kv[0].count("/"), -kv[1]))
    d    = [p for p, _ in ords]
    return (d[0] if d else ""), (d[1] if len(d) > 1 else ""),            (d[2] if len(d) > 2 else ""), len(d), "Classificada"


def classificar(titulo: str, abstract: str) -> tuple:
    """
    Classifica uma patente em até 4 tentativas, da mais completa
    para a mais simples:

      1. Título + Abstract  (score >= 2)         → status "Classificada"
      2. Fallback score-1 em Título + Abstract   → status "Classificada (Confianca Baixa)"
      3. Só Título          (score >= 2)         → status "Classificada (Pelo Titulo)"
      4. Fallback score-1 em Só Título           → status "Classificada (Titulo, Confianca Baixa)"

    Retorna (p1, p2, p3, n_matches, status).
    """
    _plac = {"nao contem resumo", "nao encontrado", "nan", "none", ""}
    resumo = abstract.strip()
    if resumo.lower() in _plac or resumo.lower().startswith("nao contem"):
        resumo = ""

    titulo_limpo = titulo.strip()
    texto_completo = f"{titulo_limpo} {resumo}".strip()
    sem_abs = not resumo

    if not texto_completo:
        return "", "", "", 0, "Sem abstract e titulo"

    # ── Tentativa 1: Título + Abstract, score >= 2 ────────────────────
    r = _classificar_por_texto(texto_completo)
    if r:
        return r

    # ── Tentativa 2: Fallback score-1 em Título + Abstract ───────────
    fb = _fallback_score1(texto_completo)
    if fb:
        return fb

    # ── Tentativas 3 e 4: Só Título (apenas se havia abstract) ───────
    # Se o texto completo já era só o título (sem_abs=True), as
    # tentativas 3 e 4 seriam idênticas às anteriores — pula.
    if titulo_limpo and not sem_abs:

        # Tentativa 3: Só Título, score >= 2
        r_titulo = _classificar_por_texto(titulo_limpo)
        if r_titulo:
            p1, p2, p3, n, _ = r_titulo
            return p1, p2, p3, n, "Classificada (Pelo Titulo)"

        # Tentativa 4: Fallback score-1 em Só Título
        fb_titulo = _fallback_score1(titulo_limpo)
        if fb_titulo:
            p1, p2, p3, n, _ = fb_titulo
            return p1, p2, p3, n, "Classificada (Titulo, Confianca Baixa)"

    return "", "", "", 0, ("Sem match (abstract vazio)" if sem_abs
                            else "Sem match de palavras")


# ══════════════════════════════════════════════════════════════════════
# UTILITARIOS DE CAMINHO E ARQUIVO
# ══════════════════════════════════════════════════════════════════════

_CHARS_INVALIDOS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_ESPACOS_DUPLOS  = re.compile(r'\s{2,}')


def _sanitizar(nome: str, max_len: int = 80) -> str:
    nome = nome.replace(_CB, "").strip()
    nome = _CHARS_INVALIDOS.sub("_", nome)
    nome = _ESPACOS_DUPLOS.sub(" ", nome).strip()
    return nome[:max_len]


def _long_path(path: str) -> str:
    """Prefixo \\\\?\\ no Windows para caminhos longos."""
    if sys.platform != "win32":
        return path
    path = os.path.abspath(path)
    if path.startswith("\\\\?\\"):
        return path
    if path.startswith("\\\\"):
        return "\\\\?\\UNC\\" + path[2:]
    return "\\\\?\\" + path



def _sem_prefixo(path: str) -> str:
    """Remove o prefixo longo adicionado pelo _long_path no Windows.
    Necessario antes de relpath/normcase para evitar ValueError quando
    um caminho tem o prefixo \\\\?\\ e o outro nao tem."""
    if path.startswith("\\\\?\\UNC\\"):
        return "\\\\" + path[8:]
    if path.startswith("\\\\?\\"):
        return path[4:]
    return path


def _pasta_do_assunto(p1: str) -> list:
    """'Pumps/PC Pump and Motor/Rotor' -> ['Pumps','PC Pump and Motor','Rotor']"""
    if not p1:
        return [_SEM_CLASS]
    return [_sanitizar(p) for p in p1.replace(_CB, "").split("/")
            if p.strip()][:3]


def _caminho_destino_pdf(p1: str) -> str:
    return os.path.join(PASTA_DESTINO, *_pasta_do_assunto(p1))


def _destino_unico(pasta: str, nome_pdf: str) -> str:
    dest = os.path.join(pasta, nome_pdf)
    if not os.path.exists(_long_path(dest)):
        return dest
    base, ext = os.path.splitext(nome_pdf)
    for i in range(1, 9999):
        tentativa = os.path.join(pasta, f"{base}_{i}{ext}")
        if not os.path.exists(_long_path(tentativa)):
            return tentativa
    return dest


def _localizar_pdf(nome_arq: str) -> str:
    """
    Localiza o PDF em PASTA_PDFS.
    Tenta: exato -> case-insensitive -> recursivo.
    Retorna o caminho ou string vazia.
    """
    if not nome_arq or not os.path.isdir(PASTA_PDFS):
        return ""
    nome_pdf = f"{nome_arq}.pdf"

    # 1. Direto
    c = os.path.join(PASTA_PDFS, nome_pdf)
    if os.path.isfile(_long_path(c)):
        return c

    # 2. Case-insensitive na raiz
    try:
        for f in os.listdir(_long_path(PASTA_PDFS)):
            if f.lower() == nome_pdf.lower():
                return os.path.join(PASTA_PDFS, f)
    except OSError:
        pass

    # 3. Recursivo
    for raiz, _, arquivos in os.walk(_long_path(PASTA_PDFS)):
        for arq in arquivos:
            if arq.lower() == nome_pdf.lower():
                return os.path.join(raiz, arq)
    return ""


def _copiar_pdf(origem: str, pasta_dest: str, nome_arq: str) -> tuple:
    """
    Cria a pasta de destino (se necessario) e copia o PDF.
    Se o arquivo JA EXISTE na pasta de destino, nao copia e retorna
    (False, "ja existe") para que o chamador possa contabilizar
    separadamente sem contar como erro nem como copia nova.
    """
    nome_pdf = f"{nome_arq}.pdf"
    dest_esperado = os.path.join(pasta_dest, nome_pdf)
    if os.path.isfile(_long_path(dest_esperado)):
        return False, "ja existe"
    try:
        os.makedirs(_long_path(pasta_dest), exist_ok=True)
        dest = _destino_unico(pasta_dest, nome_pdf)
        shutil.copy2(_long_path(origem), _long_path(dest))
        return True, dest
    except (OSError, shutil.Error) as e:
        return False, str(e)


def _localizar_em_organizada(nome_arq: str) -> str:
    """
    Procura o PDF DENTRO de PASTA_DESTINO (pasta ja organizada).
    Retorna o caminho completo ou string vazia.
    """
    if not nome_arq or not os.path.isdir(PASTA_DESTINO):
        return ""
    nome_pdf = f"{nome_arq}.pdf"
    for raiz, _, arquivos in os.walk(_long_path(PASTA_DESTINO)):
        for arq in arquivos:
            if arq.lower() == nome_pdf.lower():
                return os.path.join(raiz, arq)
    return ""


def _mover_para_nova_pasta(nome_arq: str, nova_pasta: str) -> tuple:
    """
    Move o PDF de onde ele esta em PASTA_DESTINO para nova_pasta.
    Se ja esta na pasta certa, nao faz nada.
    Apaga pastas vazias apos o movimento.
    Retorna (moveu: bool, pasta_anterior: str, mensagem: str).
    """
    caminho_atual = _localizar_em_organizada(nome_arq)
    if not caminho_atual:
        return False, "", "nao encontrado em patents_organized"

    pasta_atual = os.path.dirname(caminho_atual)

    # Normaliza os dois caminhos para comparar
    if os.path.normcase(_sem_prefixo(os.path.abspath(pasta_atual))) == \
       os.path.normcase(_sem_prefixo(os.path.abspath(nova_pasta))):
        return False, pasta_atual, "ja na pasta correta"

    try:
        os.makedirs(_long_path(nova_pasta), exist_ok=True)
        dest = _destino_unico(nova_pasta, f"{nome_arq}.pdf")
        shutil.move(_long_path(caminho_atual), _long_path(dest))
        # Remove pasta anterior se ficou vazia
        try:
            os.removedirs(pasta_atual)
        except OSError:
            pass
        return True, pasta_atual, dest
    except (OSError, shutil.Error) as e:
        return False, pasta_atual, str(e)


# ══════════════════════════════════════════════════════════════════════
# FORMATACAO EXCEL
# ══════════════════════════════════════════════════════════════════════

_FILLS = {
    "Classificada":                           PatternFill("solid", fgColor="C6EFCE"),  # verde
    "Classificada (Confianca Baixa)":         PatternFill("solid", fgColor="D9E1F2"),  # azul claro
    "Classificada (Pelo Titulo)":             PatternFill("solid", fgColor="FFF2CC"),  # amarelo claro
    "Classificada (Titulo, Confianca Baixa)": PatternFill("solid", fgColor="FCE4D6"),  # laranja claro
    "Ja classificada (mantida)":              PatternFill("solid", fgColor="E2EFDA"),  # verde muito claro
    "Sem classificacao":                 PatternFill("solid", fgColor="FFC7CE"),
    "Sem match de palavras":             PatternFill("solid", fgColor="FFC7CE"),
    "Sem match (abstract vazio)":        PatternFill("solid", fgColor="FFEB9C"),
    "Sem abstract e titulo":             PatternFill("solid", fgColor="FFEB9C"),
    "PDF nao encontrado":                PatternFill("solid", fgColor="FFEB9C"),
    "Erro ao copiar":                    PatternFill("solid", fgColor="FF7F7F"),
}
_FH  = PatternFill("solid", fgColor="1F4E79")
_FNT = Font(bold=True, color="FFFFFF", size=11)
_FN  = Font(size=10)
_AL  = Alignment(horizontal="left",   vertical="center", wrap_text=True)
_AC  = Alignment(horizontal="center", vertical="center", wrap_text=True)
_BRD = Border(left=Side(style="thin"),  right=Side(style="thin"),
               top=Side(style="thin"),   bottom=Side(style="thin"))


def _salvar_planilha(df: pd.DataFrame, status_linhas: list):
    """Salva o DataFrame e aplica cores nas colunas de assunto."""
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.freeze_panes = "A2"

    cab = {ws.cell(1, c).value: c for c in range(1, ws.max_column + 1)}
    cols_assunto = [cab[c] for c in
                    ("Assunto Primario", "Assunto Secundario", "Assunto Terciario")
                    if c in cab]

    for i, status in enumerate(status_linhas, start=2):
        fill = _FILLS.get(status, PatternFill())
        for c in cols_assunto:
            cell      = ws.cell(i, c)
            cell.fill = fill
            cell.font = _FN
            cell.alignment = _AL
            cell.border    = _BRD

    wb.save(EXCEL_FILE)


def _gerar_relatorio(registros: list):
    """Gera planilha de relatorio com aba de detalhes e aba de resumo."""
    colunas = ["Codigo", "Nome do Arquivo", "Assunto Primario",
               "Assunto Secundario", "Assunto Terciario",
               "Status", "PDF Origem", "PDF Destino", "Obs"]

    pd.DataFrame(registros, columns=colunas).to_excel(
        RELATORIO, index=False, engine="openpyxl")

    wb = load_workbook(RELATORIO)
    ws = wb.active
    ws.title = "Relatorio"
    larguras = {"Codigo": 22, "Nome do Arquivo": 48,
                "Assunto Primario": 45, "Assunto Secundario": 45, "Assunto Terciario": 45,
                "Status": 32, "PDF Origem": 55, "PDF Destino": 55, "Obs": 40}

    for i, col in enumerate(colunas, 1):
        c = ws.cell(1, i)
        c.fill = _FH; c.font = _FNT; c.alignment = _AC; c.border = _BRD
        ws.column_dimensions[c.column_letter].width = larguras.get(col, 20)
    ws.row_dimensions[1].height = 26

    col_status = colunas.index("Status") + 1
    for r, reg in enumerate(registros, 2):
        fill = _FILLS.get(reg.get("Status", ""), PatternFill())
        for c in range(1, len(colunas) + 1):
            cell = ws.cell(r, c)
            cell.font = _FN; cell.alignment = _AL; cell.border = _BRD
            if c == col_status:
                cell.fill = fill

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = (
        f"A1:{ws.cell(1, len(colunas)).column_letter}{len(registros)+1}"
    )

    # Aba resumo por pasta raiz
    ws2 = wb.create_sheet("Resumo por Pasta")
    ws2.append(["Pasta Primaria", "Qtd. Patentes"])
    for c in range(1, 3):
        cell = ws2.cell(1, c)
        cell.fill = _FH; cell.font = _FNT
        cell.alignment = _AC; cell.border = _BRD
    ws2.column_dimensions["A"].width = 50
    ws2.column_dimensions["B"].width = 16

    cont_resumo = defaultdict(int)
    for reg in registros:
        p = (reg.get("Assunto Primario") or _SEM_CLASS)
        raiz = p.replace(_CB, "").split("/")[0]
        cont_resumo[raiz] += 1
    for pasta, qtd in sorted(cont_resumo.items(), key=lambda x: (-x[1], x[0])):
        ws2.append([pasta, qtd])
        row = ws2.max_row
        for c in range(1, 3):
            cell = ws2.cell(row, c)
            cell.font = _FN; cell.alignment = _AL; cell.border = _BRD
    ws2.freeze_panes = "A2"

    wb.save(RELATORIO)


# ══════════════════════════════════════════════════════════════════════
# IMPRESSAO NO TERMINAL
# ══════════════════════════════════════════════════════════════════════

SEP = "=" * 64


def _imprimir_resumo(cont: dict, total: int, modo: str):
    print(f"\n{SEP}")
    print(f"  RESUMO — {modo.upper()}")
    print(SEP)
    print(f"  Total de linhas processadas    : {total:>6}")
    if cont.get("mantida", 0):
        print(f"  Ja classificadas (mantidas)    : {cont['mantida']:>6}  <- nao alteradas")
    novas = cont.get("class", 0) + cont.get("cb", 0)
    print(f"  Novas / reclassificadas        : {novas:>6}")
    print(f"    - score >= 2                 : {cont.get('class',0):>6}")
    print(f"    - confianca baixa (score 1)  : {cont.get('cb',0):>6}")
    print(f"  Sem classificacao              : {cont.get('sem',0):>6}")
    print()
    print(f"  PDFs copiados (novos)          : {cont.get('copiado',0):>6}")
    if cont.get("ja_existe", 0):
        print(f"  PDFs ja na pasta correta       : {cont['ja_existe']:>6}  <- nao duplicados")
    if cont.get("realocado", 0):
        print(f"  PDFs realocados (nova pasta)   : {cont['realocado']:>6}  <- movidos dentro de patents_organized")
    print(f"  PDFs nao encontrados           : {cont.get('nao_enc',0):>6}")
    print(f"  Erros de copia                 : {cont.get('erro',0):>6}")
    print(SEP)


def _imprimir_arvore(por_pasta: dict):
    if not por_pasta:
        return
    print(f"\n{SEP}")
    print("  DISTRIBUICAO POR PASTA")
    print(SEP)
    raizes: dict = defaultdict(lambda: {"total": 0, "filhas": defaultdict(int)})
    for pasta, qtd in por_pasta.items():
        partes = pasta.split("/")
        raiz   = partes[0]
        raizes[raiz]["total"] += qtd
        if len(partes) > 1:
            raizes[raiz]["filhas"]["/".join(partes[:2])] += qtd
    for raiz in sorted(raizes):
        info = raizes[raiz]
        print(f"\n  [+] {raiz}  ({info['total']})")
        filhas = sorted(info["filhas"].items())
        for i, (f2, qtd) in enumerate(filhas):
            conn = "L-" if i == len(filhas) - 1 else "+-"
            print(f"       {conn} {f2.split('/')[-1]}  ({qtd})")
    print()


# ══════════════════════════════════════════════════════════════════════
# NUCLEO DE PROCESSAMENTO
# ══════════════════════════════════════════════════════════════════════

def _processar(df: pd.DataFrame, modo: str) -> tuple:
    """
    Processa todas as linhas do DataFrame conforme o modo escolhido.

    modo 'novas':
        Classifica apenas linhas com Assunto Primario vazio.
        Copia o PDF para a pasta correspondente.
        Linhas ja classificadas sao mantidas intactas.

    modo 'reprocessar':
        Reclassifica TODAS as linhas, sem excecao.
        Remove a copia antiga do PDF de onde quer que esteja em PASTA_DESTINO
        e copia o arquivo para a pasta da nova classificacao.

    modo 'so_copiar':
        Nao altera nenhuma classificacao na planilha.
        Usa o Assunto Primario existente e apenas copia o PDF para
        a pasta correspondente (util para popular a estrutura de pastas
        apos importar uma planilha ja classificada externamente).

    Retorna: (registros_relatorio, status_por_linha, contadores, por_pasta)
    """
    registros: list     = []
    status_linhas: list = []
    cont      = defaultdict(int)
    por_pasta = defaultdict(int)
    total     = len(df)

    for idx, row in df.iterrows():
        codigo   = str(row.get("Codigo",         "") or "").strip()
        nome_arq = str(row.get("Nome do Arquivo", "") or "").strip()
        titulo   = str(row.get("Titulo",          "") or "").strip()
        abstract = str(row.get("Abstract",        "") or "").strip()

        # Suporte aos dois nomes de coluna possiveis no Excel
        if not codigo:
            codigo   = str(row.get("C\u00f3digo", "") or "").strip()
        if not titulo:
            titulo   = str(row.get("T\u00edtulo", "") or "").strip()
        if not nome_arq:
            nome_arq = str(row.get("Nome do Arquivo", "") or "").strip()

        p1_ant = str(row.get("Assunto Primario",   "") or "").strip()
        p2_ant = str(row.get("Assunto Secundario", "") or "").strip()
        p3_ant = str(row.get("Assunto Terciario",  "") or "").strip()
        ja_classificada = bool(p1_ant
                              and p1_ant.lower() not in ("nan", "", "nao classificada"))

        # ── 1. Decisao de classificacao ───────────────────────────────
        if modo == "so_copiar":
            # Usa o que ja esta na planilha; nao reclassifica
            p1, p2, p3   = p1_ant, p2_ant, p3_ant
            reclassificou = False
            if ja_classificada:
                status_class = "Ja classificada (mantida)"
                cont["mantida"] += 1
            else:
                status_class = "Sem classificacao"
                cont["sem"] += 1

        elif modo == "novas" and ja_classificada:
            # Modo incremental: linha ja preenchida — pula a classificacao
            p1, p2, p3    = p1_ant, p2_ant, p3_ant
            reclassificou = False
            status_class  = "Ja classificada (mantida)"
            cont["mantida"] += 1

        else:
            # Classifica: linha nova (modo 'novas') ou modo 'reprocessar'
            p1, p2, p3, _, status_class = classificar(titulo, abstract)
            reclassificou = True
            df.at[idx, "Assunto Primario"]   = p1
            df.at[idx, "Assunto Secundario"] = p2
            df.at[idx, "Assunto Terciario"]  = p3

            if p1:
                if status_class == "Classificada (Titulo, Confianca Baixa)":
                    cont["titulo_cb"] += 1
                elif status_class == "Classificada (Pelo Titulo)":
                    cont["titulo"] += 1
                elif _CB in p1:
                    cont["cb"] += 1
                else:
                    cont["class"] += 1
            else:
                cont["sem"] += 1
                # Grava "Nao Classificada" na planilha para que a linha
                # seja reconhecida nas proximas execucoes e nao fique como
                # vazia (o que faria o modo 'novas' tentar reclassificar infinitamente)
                p1 = "Nao Classificada"
                df.at[idx, "Assunto Primario"]   = "Nao Classificada"
                df.at[idx, "Assunto Secundario"] = ""
                df.at[idx, "Assunto Terciario"]  = ""

        if p1 and p1 != "Nao Classificada":
            por_pasta[p1.replace(_CB, "")] += 1

        # ── 2. Processamento do PDF ───────────────────────────────────
        pdf_origem  = ""
        pdf_destino = ""
        obs         = ""

        if not nome_arq:
            obs = "Sem nome de arquivo"

        elif not reclassificou:
            # Linha ja estava classificada e nao foi reclassificada agora
            # → o PDF ja deve estar na pasta correta, nao copia novamente
            cont["ja_existe"] += 1
            obs = "Ja classificada — PDF nao recopiado"

        else:
            caminho_origem = _localizar_pdf(nome_arq)

            if not caminho_origem:
                cont["nao_enc"] += 1
                obs = "PDF nao encontrado na pasta de origem"

            else:
                pdf_origem = caminho_origem

                pasta_dest = _caminho_destino_pdf(p1)

                if modo == "reprocessar" and reclassificou:
                    # ── REPROCESSAR: trabalha SÓ dentro de patents_organized ──
                    # Verifica se o PDF já existe lá dentro
                    moveu, pasta_ant, msg_mov = _mover_para_nova_pasta(
                        nome_arq, pasta_dest)

                    if moveu:
                        # Mudou de pasta — arquivo foi movido
                        cont["realocado"] += 1
                        pasta_ant_nome = os.path.basename(pasta_ant)
                        obs         = f"Movido de: {pasta_ant_nome}"
                        pdf_destino = msg_mov
                    elif "ja na pasta correta" in msg_mov:
                        # Classificacao mudou na planilha mas pasta é a mesma
                        obs         = "Pasta inalterada (classificacao equivalente)"
                        pdf_destino = _localizar_em_organizada(nome_arq)
                    elif "nao encontrado em patents_organized" in msg_mov:
                        # PDF ainda nao estava organizado — copia da origem
                        ok, msg_copia = _copiar_pdf(caminho_origem, pasta_dest, nome_arq)
                        if ok:
                            cont["copiado"] += 1
                            pdf_destino = msg_copia
                            obs = "Copiado (nao estava organizado)"
                        else:
                            cont["erro"] += 1
                            obs = f"Erro ao copiar: {msg_copia}"
                            status_class = "Erro ao copiar"
                    else:
                        cont["erro"] += 1
                        obs = f"Erro ao mover: {msg_mov}"
                        status_class = "Erro ao copiar"

                else:
                    # ── NOVAS / SO_COPIAR: copia da origem (primeira vez) ──
                    ok, msg = _copiar_pdf(caminho_origem, pasta_dest, nome_arq)
                    if ok:
                        cont["copiado"] += 1
                        pdf_destino = msg
                        if not obs:
                            obs = "OK"
                    elif msg == "ja existe":
                        cont["ja_existe"] += 1
                        pdf_destino = os.path.join(pasta_dest, f"{nome_arq}.pdf")
                        obs = "PDF ja estava na pasta correta"
                    else:
                        cont["erro"] += 1
                        obs          = f"Erro: {msg}"
                        status_class = "Erro ao copiar"

        # Status final para coloracao da planilha
        if not p1:
            status_final = "Sem classificacao"
        elif "Erro" in obs:
            status_final = "Erro ao copiar"
        elif "nao encontrado" in obs.lower():
            status_final = "PDF nao encontrado"
        elif status_class == "Ja classificada (mantida)":
            status_final = "Ja classificada (mantida)"
        elif _CB in (p1 or ""):
            status_final = "Classificada (Confianca Baixa)"
        else:
            status_final = "Classificada"

        status_linhas.append(status_final)

        registros.append({
            "Codigo":             codigo,
            "Nome do Arquivo":    nome_arq,
            "Assunto Primario":   p1,
            "Assunto Secundario": p2,
            "Assunto Terciario":  p3,
            "Status":             status_class,
            "PDF Origem":         pdf_origem,
            "PDF Destino":        pdf_destino,
            "Obs":                obs,
        })

        # Progresso no terminal
        n = idx + 1
        if n % 200 == 0 or n == total:
            print(f"  ... {n}/{total}  "
                  f"[class: {cont['class']+cont['cb']} | "
                  f"mantidas: {cont['mantida']} | "
                  f"pdfs: {cont['copiado']}]")

    return registros, status_linhas, dict(cont), dict(por_pasta)


# ══════════════════════════════════════════════════════════════════════
# EXECUTOR
# ══════════════════════════════════════════════════════════════════════

_NOMES_MODO = {
    "novas":       "Classificar novas patentes + copiar PDFs",
    "reprocessar": "Reprocessar TUDO + realocar PDFs",
    "so_copiar":   "Apenas copiar PDFs (sem reclassificar)",
}


def _executar(modo: str):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{SEP}")
    print(f"  {_NOMES_MODO[modo]}  -  {agora}")
    print(SEP)

    if not os.path.exists(EXCEL_FILE):
        print(f"\n  X Planilha nao encontrada: {EXCEL_FILE}")
        return

    if not os.path.isdir(PASTA_PDFS):
        print(f"\n  ! Pasta de PDFs nao encontrada: {PASTA_PDFS}")
        print("    A classificacao sera feita, mas os PDFs nao serao copiados.")

    print(f"\n  Lendo planilha: {EXCEL_FILE}")
    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
    print(f"  {len(df)} linhas carregadas.\n")

    # Garante que as colunas existem e sao do tipo object (string)
    # Colunas vazias no Excel sao lidas como float64 — forcamos object
    for col in ("Assunto Primario", "Assunto Secundario", "Assunto Terciario"):
        if col not in df.columns:
            df[col] = ""
        else:
            df[col] = df[col].astype(object).where(df[col].notna(), "")

    registros, status_linhas, cont, por_pasta = _processar(df, modo)

    print(f"\n  Salvando planilha: {EXCEL_FILE}")
    _salvar_planilha(df, status_linhas)
    print("  OK Planilha salva.")

    print(f"\n  Gerando relatorio: {RELATORIO}")
    try:
        os.makedirs(os.path.dirname(os.path.abspath(RELATORIO)), exist_ok=True)
        _gerar_relatorio(registros)
        print("  OK Relatorio salvo.")
    except Exception as e:
        print(f"  ! Nao foi possivel salvar o relatorio: {e}")

    _imprimir_resumo(cont, len(df), _NOMES_MODO[modo])
    _imprimir_arvore(por_pasta)

    print(f"  Planilha  : {EXCEL_FILE}")
    print(f"  Relatorio : {RELATORIO}")
    print(f"  PDFs em   : {PASTA_DESTINO}")
    print(f"\n{SEP}\n")


# ══════════════════════════════════════════════════════════════════════
# VERIFICACAO DE CONSISTENCIA
# ══════════════════════════════════════════════════════════════════════

def verificar_consistencia():
    """
    Compara a planilha com a pasta patents_organized e reporta:

      1. Patentes na planilha x PDFs nas pastas
         - Linha classificada sem PDF na pasta esperada (falta o arquivo)
         - PDF na pasta sem correspondente na planilha (arquivo orfao)

      2. Desalinhamentos de pasta
         - Linha diz "Pumps/PC Pump" mas o PDF esta em "Pumps/Screw Pump"

      3. Contagem geral de consistencia
    """
    sep2 = "-" * 64

    print(f"\n{SEP}")
    print("  VERIFICACAO DE CONSISTENCIA")
    print(SEP)

    if not os.path.exists(EXCEL_FILE):
        print(f"\n  X Planilha nao encontrada: {EXCEL_FILE}")
        return

    print(f"\n  Lendo planilha: {EXCEL_FILE}")
    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
    n_linhas = len(df)
    print(f"  {n_linhas} linhas carregadas.")

    if not os.path.isdir(PASTA_DESTINO):
        print(f"\n  X Pasta organizada nao encontrada: {PASTA_DESTINO}")
        print("    Execute primeiro as opcoes 1 ou 3 para organizar os PDFs.")
        return

    # ── Indexa todos os PDFs existentes em PASTA_DESTINO ─────────────
    # { nome_sem_extensao.lower() : caminho_completo }
    pdfs_em_disco: dict = {}
    for raiz, _, arquivos in os.walk(_long_path(PASTA_DESTINO)):
        for arq in arquivos:
            if arq.lower().endswith(".pdf"):
                stem = os.path.splitext(arq)[0].lower()
                pdfs_em_disco[stem] = os.path.join(raiz, arq)

    print(f"  {len(pdfs_em_disco)} PDFs encontrados em patents_organized.\n")

    # ── Percorre a planilha linha por linha ───────────────────────────
    ok            = 0   # linha classif. + PDF na pasta certa
    sem_pdf_disco = []  # classificada mas PDF ausente da pasta
    pasta_errada  = []  # PDF existe mas em pasta diferente da planilha
    nao_class     = []  # "Nao Classificada" ou vazia
    sem_nome      = []  # sem nome de arquivo na coluna

    nomes_na_planilha = set()

    for _, row in df.iterrows():
        codigo   = str(row.get("Codigo", "") or row.get("C\u00f3digo", "") or "").strip()
        nome_arq = str(row.get("Nome do Arquivo", "") or "").strip()
        p1       = str(row.get("Assunto Primario", "") or "").strip()

        if not nome_arq or nome_arq.lower() in ("nan", ""):
            sem_nome.append(codigo)
            continue

        nomes_na_planilha.add(nome_arq.lower())

        p1_limpo = p1.replace(_CB, "").strip()
        nao_classificada = (not p1_limpo
                            or p1_limpo.lower() in ("nan", "", "nao classificada"))

        if nao_classificada:
            nao_class.append((codigo, nome_arq, p1_limpo or "(vazio)"))
            continue

        # Pasta esperada conforme a planilha
        pasta_esperada = _caminho_destino_pdf(p1_limpo)
        pdf_esperado   = os.path.join(pasta_esperada, f"{nome_arq}.pdf")

        stem = nome_arq.lower()

        if stem not in pdfs_em_disco:
            # PDF nao esta em NENHUMA subpasta de patents_organized
            sem_pdf_disco.append((codigo, nome_arq, p1_limpo))
        else:
            caminho_real = pdfs_em_disco[stem]
            pasta_real   = os.path.dirname(caminho_real)

            if os.path.normcase(_sem_prefixo(os.path.abspath(pasta_real))) == \
               os.path.normcase(_sem_prefixo(os.path.abspath(pasta_esperada))):
                ok += 1
            else:
                # PDF existe mas em pasta diferente da planilha
                pasta_real_rel = os.path.relpath(_sem_prefixo(pasta_real), _sem_prefixo(PASTA_DESTINO))
                pasta_esp_rel  = os.path.relpath(_sem_prefixo(pasta_esperada), _sem_prefixo(PASTA_DESTINO))
                pasta_errada.append((codigo, nome_arq,
                                     pasta_esp_rel, pasta_real_rel))

    # PDFs em disco sem correspondente na planilha (orfaos)
    orfaos = [
        os.path.relpath(_sem_prefixo(caminho), _sem_prefixo(PASTA_DESTINO))
        for stem, caminho in pdfs_em_disco.items()
        if stem not in nomes_na_planilha
    ]

    # ── Exibe resultado ───────────────────────────────────────────────
    total_class = n_linhas - len(nao_class) - len(sem_nome)

    print(f"  {sep2}")
    print(f"  CONTAGEM GERAL")
    print(f"  {sep2}")
    print(f"  Linhas na planilha            : {n_linhas:>6}")
    print(f"  Sem nome de arquivo           : {len(sem_nome):>6}")
    print(f"  Nao classificadas             : {len(nao_class):>6}")
    print(f"  Classificadas (total)         : {total_class:>6}")
    print(f"    OK — PDF na pasta correta   : {ok:>6}")
    print(f"    PROBLEMA — PDF ausente      : {len(sem_pdf_disco):>6}")
    print(f"    PROBLEMA — pasta errada     : {len(pasta_errada):>6}")
    print(f"  PDFs em disco                 : {len(pdfs_em_disco):>6}")
    print(f"  PDFs orfaos (sem linha)       : {len(orfaos):>6}")

    consistente = (len(sem_pdf_disco) == 0
                   and len(pasta_errada) == 0
                   and len(orfaos) == 0)
    print()
    if consistente:
        print("  RESULTADO: planilha e pastas estao consistentes.")
    else:
        print("  RESULTADO: foram encontrados problemas (detalhes abaixo).")

    # ── Detalhes dos problemas ────────────────────────────────────────
    if sem_pdf_disco:
        print(f"\n  {sep2}")
        print(f"  PDFs AUSENTES ({len(sem_pdf_disco)}) — classificados na planilha mas nao encontrados")
        print(f"  {sep2}")
        for cod, nome, p1 in sem_pdf_disco:
            print(f"  [{cod:<22}]  {nome}")
            print(f"     esperado em: {os.path.relpath(_sem_prefixo(_caminho_destino_pdf(p1)), _sem_prefixo(PASTA_DESTINO))}")

    if pasta_errada:
        print(f"\n  {sep2}")
        print(f"  PASTA ERRADA ({len(pasta_errada)}) — PDF existe mas nao onde a planilha indica")
        print(f"  {sep2}")
        for cod, nome, esperada, real in pasta_errada:
            print(f"  [{cod:<22}]  {nome}")
            print(f"     planilha diz : {esperada}")
            print(f"     esta em      : {real}")

    if orfaos:
        print(f"\n  {sep2}")
        print(f"  ORFAOS ({len(orfaos)}) — PDFs em disco sem linha na planilha")
        print(f"  {sep2}")
        for caminho in sorted(orfaos):
            print(f"  {caminho}")

    if nao_class:
        print(f"\n  {sep2}")
        print(f"  NAO CLASSIFICADAS ({len(nao_class)}) — sem assunto primario definido")
        print(f"  {sep2}")
        for cod, nome, p1 in nao_class:
            print(f"  [{cod:<22}]  {nome}  ({p1})")

    print(f"\n{SEP}\n")


# ══════════════════════════════════════════════════════════════════════
# MENU INTERATIVO
# ══════════════════════════════════════════════════════════════════════

def _exibir_config():
    pdfs_ok  = "OK" if os.path.isdir(PASTA_PDFS)   else "X nao encontrada"
    excel_ok = "OK" if os.path.isfile(EXCEL_FILE)   else "X nao encontrado"
    dest_ok  = "OK" if os.path.isdir(PASTA_DESTINO) else "(sera criada automaticamente)"
    print()
    print(f"  Planilha de patentes  : {EXCEL_FILE}")
    print(f"                          [{excel_ok}]")
    print(f"  Pasta de PDFs origem  : {PASTA_PDFS}")
    print(f"                          [{pdfs_ok}]")
    print(f"  Pasta organizada      : {PASTA_DESTINO}")
    print(f"                          [{dest_ok}]")
    print(f"  Relatorio de operacao : {RELATORIO}")
    print(f"  Pastas no dicionario  : {len(PALAVRAS_CHAVE)}")


def _confirmar(msg: str) -> bool:
    resp = input(f"\n  {msg} [s/N]: ").strip().lower()
    return resp in ("s", "sim", "y", "yes")


def menu():
    while True:
        print(f"\n{SEP}")
        print("  ORGANIZADOR DE PATENTES")
        print(SEP)
        print()
        print("  1  Classificar novas patentes + copiar PDFs")
        print("     Processa apenas linhas com 'Assunto Primario' vazio.")
        print("     Linhas ja classificadas sao ignoradas.")
        print()
        print("  2  Reprocessar TUDO + realocar PDFs")
        print("     Reclassifica TODAS as linhas da planilha.")
        print("     Remove o PDF da pasta antiga e copia para a nova.")
        print()
        print("  3  Apenas copiar PDFs  (sem reclassificar)")
        print("     Usa a classificacao ja existente na planilha.")
        print("     Copia os PDFs para a estrutura de pastas correspondente.")
        print()
        print("  4  Verificar consistencia (planilha x pastas)")
        print("     Confere se cada linha da planilha tem o PDF na pasta")
        print("     correta e detecta arquivos orfaos ou ausentes.")
        print()
        print("  5  Ver configuracao de caminhos")
        print()
        print("  0  Sair")
        print(SEP)

        opcao = input("  Escolha uma opcao: ").strip()

        if opcao == "0":
            print("\n  Ate logo!\n")
            break

        elif opcao == "1":
            print(f"\n{SEP}")
            print("  OPCAO 1 — Classificar novas patentes")
            print(SEP)
            print("  Somente as linhas com 'Assunto Primario' vazio serao")
            print("  classificadas. As demais permanecem exatamente como estao.")
            if _confirmar("Confirmar execucao?"):
                _executar("novas")
            else:
                print("\n  Operacao cancelada.")

        elif opcao == "2":
            print(f"\n{SEP}")
            print("  OPCAO 2 — Reprocessar TUDO")
            print(SEP)
            print("  ATENCAO: todas as classificacoes serao recalculadas,")
            print("  incluindo as que foram editadas manualmente na planilha.")
            print("  Os PDFs serao removidos das pastas atuais e copiados")
            print("  para as pastas correspondentes as novas classificacoes.")
            if _confirmar("Confirmar reprocessamento completo?"):
                _executar("reprocessar")
            else:
                print("\n  Operacao cancelada.")

        elif opcao == "3":
            print(f"\n{SEP}")
            print("  OPCAO 3 — Copiar PDFs sem reclassificar")
            print(SEP)
            print("  A classificacao na planilha nao sera alterada.")
            print("  Os PDFs serao copiados para a pasta correspondente")
            print("  ao 'Assunto Primario' ja registrado em cada linha.")
            if _confirmar("Confirmar copia dos PDFs?"):
                _executar("so_copiar")
            else:
                print("\n  Operacao cancelada.")

        elif opcao == "4":
            verificar_consistencia()

        elif opcao == "5":
            print(f"\n{SEP}")
            print("  CONFIGURACAO DE CAMINHOS")
            print(SEP)
            _exibir_config()

        else:
            print("\n  Opcao invalida. Digite 0, 1, 2, 3, 4 ou 5.")

        input("\n  Pressione Enter para voltar ao menu...")


# ══════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    menu()
