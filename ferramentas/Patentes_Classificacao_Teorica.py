"""
auditoria_classificacao.py
──────────────────────────
Gera uma planilha de auditoria da classificação de patentes.

O que FAZ:
  • Lê a planilha principal de patentes (EXCEL_FILE)
  • Reclassifica cada patente usando palavras_chave.py
  • Gera uma nova planilha de relatório com:
      Código | Nome do Arquivo | Pasta Primária | Pasta Secundária | Pasta Terciária | Status
  • Imprime no terminal um resumo em árvore com contagens por pasta

O que NÃO FAZ:
  • Não move, copia nem altera nenhum arquivo
  • Não modifica a planilha principal

Uso:
  python auditoria_classificacao.py
  python auditoria_classificacao.py --excel outro_arquivo.xlsx
  python auditoria_classificacao.py --saida meu_relatorio.xlsx
  python auditoria_classificacao.py --testes          (apenas regressão)
  python auditoria_classificacao.py --comparar        (relatório antes/depois)

═══════════════════════════════════════════════════════════════════════
CHANGELOG — Parte A: Algoritmo de classificação refatorado
═══════════════════════════════════════════════════════════════════════

Problema identificado (Causa 1 — 71% dos casos):
  A pasta raiz "Valves" acumulava 3-5 hits baratos com termos genéricos
  de 1 palavra ("valve", "valve assembly") e vencia sistematicamente
  sobre subpastas específicas que tinham termos melhores mas menos hits.

Três correções aplicadas:

  1. SCORING PONDERADO POR ESPECIFICIDADE
     Antes: cada match valia 1 ponto (flat).
     Agora: termos de 1 palavra = 1 pt | 2 palavras = 2 pts | 3+ = 3 pts.
     Isso reduz a vantagem das raízes com muitos termos ultra-genéricos.

  2. FILTRO HIERÁRQUICO
     Antes: pai e filha competiam no mesmo ranking de score.
     Agora: se qualquer filha tem score ≥ SCORE_MINIMO, o pai é suprimido
     antes da ordenação final. A subpasta mais específica sempre vence
     sobre seu ancestral — independente da contagem bruta.

  3. ORDENAÇÃO POR PROFUNDIDADE PRIMEIRO
     Antes: key=(-score, -profundidade)  → score vencia, profundidade era
            desempate → raiz com muitos hits simples ganhava.
     Agora: key=(-profundidade, -score)  → subpasta mais específica
            vence; score desempata dentro do mesmo nível.

═══════════════════════════════════════════════════════════════════════
CHANGELOG V18 (Abril 2026) — Auditoria Completa
═══════════════════════════════════════════════════════════════════════

Análise de 5977 patentes revelou 31 "sem match" (0.5%) e 396 baixa
confiança (6.5%). Correções implementadas:

  4. EXCLUSÃO SEMÂNTICA (nova função _aplicar_exclusao_semantica)
     Patentes de domínio médico ("heart valve", "cardiac pump", "insulin
     pump") eram classificadas erroneamente em categorias de engenharia.
     Agora, se termos de exclusão aparecem no texto, a categoria raiz
     correspondente é removida antes do ranking final.
     Dicionário EXCLUSAO_SEMANTICA em palavras_chave.py define os pares
     (categoria, termos_bloqueadores).

  5. NOVOS TERMOS NO DICIONÁRIO (V18 em palavras_chave.py)
     • Pumps: +20 termos (spiral pump, eccentric pump, pumping fluid,
       bomba de alimentação, bomba de fluxo, etc.)
     • Pumps/PC Pump and Motor: +7 termos (eccentric spiral pump,
       progressive cavity apparatus, pdm rotor, etc.)
     • Pumps/PC Pump and Motor/Rotor: +3 termos (conjugate rotor,
       rotor stator design)
     • Grinding and Milling: +11 termos (kneading machine, hackrotor,
       rotor-stator system, etc.)
     • Bearings: +1 termo (bearing gearing section)
     Total: 43 termos novos (ver bloco _ADICOES_V18_AUDITORIA).

RESULTADO V18:
  • Sem match:         31 → 3   (-90%)
  • Baixa confiança:  396 → 383 (-3%)
  • Classificadas:   5550 → 5591 (+41)
  • Regressões:       apenas 2 patentes
"""

import os
import re
import sys
import argparse
import pathlib
from collections import defaultdict

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

# ══════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO — ajuste os caminhos conforme seu ambiente
# ══════════════════════════════════════════════════════════════════════

EXCEL_FILE  = r"C:\Projetos\Testes_Prog_Patente\Projeto\patents_data_test.xlsx"
SAIDA_FILE  = r"C:\Projetos\Testes_Prog_Patente\Projeto\auditoria_classificacao.xlsx"

# Pontuação mínima para considerar match.
# Com scoring ponderado: um termo de 2 palavras já vale 2 pts (passa o limiar);
# um único "valve" (1 pt) não passa mais sozinho.
SCORE_MINIMO = 2

# ══════════════════════════════════════════════════════════════════════
# CARREGA PALAVRAS-CHAVE (mesmo arquivo do classificador)
# ══════════════════════════════════════════════════════════════════════

SCRIPT_DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

try:
    # Tenta importar diretamente (palavras_chave.py na mesma pasta do script)
    from palavras_chave import PALAVRAS_CHAVE, EXCLUSAO_SEMANTICA, PRIORIDADE_TITULO
except ImportError:
    try:
        # Fallback: tenta importar via caminho completo do projeto
        from Testes_Prog_Patente.Projeto.Prog_Patente.Prog_aux.palavras_chave import PALAVRAS_CHAVE, EXCLUSAO_SEMANTICA, PRIORIDADE_TITULO
    except ImportError:
        print(f"\n  ✖ Arquivo palavras_chave.py não encontrado em: {SCRIPT_DIR}")
        print("  Coloque palavras_chave.py na mesma pasta deste script.\n")
        raise SystemExit(1)

# ── Pré-compila padrões + calcula peso de cada termo ─────────────────
# Tupla: (termo, padrão_compilado, peso_int)
# O peso é calculado uma única vez aqui para evitar split() repetido.
_COMPILED: dict = {}

for _pasta, _palavras in PALAVRAS_CHAVE.items():
    entradas = []
    for _termo in _palavras:
        _n = len(_termo.split())
        # Pesos por especificidade:
        #   3+ palavras → 3 pts  (ex: "pressure relief valve")
        #   2 palavras  → 2 pts  (ex: "check valve")
        #   1 palavra   → 1 pt   (ex: "valve")
        _peso = 3 if _n >= 3 else (2 if _n == 2 else 1)
        entradas.append((_termo, re.compile(re.escape(_termo.lower())), _peso))
    _COMPILED[_pasta] = entradas

# ── Pré-compila padrões de exclusão semântica (V18) ──────────────────
# Se um termo de exclusão é encontrado no texto, a categoria raiz
# correspondente é bloqueada. Impede que patentes médicas
# ("heart valve", "cardiac pump") caiam em Valves/Pumps de engenharia.
_COMPILED_EXCLUSAO: dict = {}
for _cat_excl, _termos_excl in EXCLUSAO_SEMANTICA.items():
    _COMPILED_EXCLUSAO[_cat_excl] = [
        re.compile(re.escape(_t.lower())) for _t in _termos_excl
    ]

# Sufixo aplicado a classificações de baixa confiança (score = 1, via fallback)
_SUFIXO_BAIXA_CONFIANCA = " (Confiança Baixa/Abstract Curto)"


# ══════════════════════════════════════════════════════════════════════
# MOTOR DE CLASSIFICAÇÃO — com Fallback Score-1 para subpastas
# ══════════════════════════════════════════════════════════════════════

def calcular_scores(texto: str, score_minimo: int = None) -> dict:
    """
    Retorna {pasta: score_ponderado} para o texto fornecido.

    CORREÇÃO 1 — Scoring ponderado por especificidade do termo:
      Termos de 1 palavra  (ex: "valve")                  → peso 1
      Termos de 2 palavras (ex: "check valve")            → peso 2
      Termos de 3+ palavras (ex: "pressure relief valve") → peso 3

    Parâmetro score_minimo: se None, usa o global SCORE_MINIMO.
    Passar score_minimo=1 activa o modo de fallback.
    """
    limiar = score_minimo if score_minimo is not None else SCORE_MINIMO
    t = texto.lower()
    scores = {}
    for pasta, entradas in _COMPILED.items():
        score = sum(peso for _, pat, peso in entradas if pat.search(t))
        if score >= limiar:
            scores[pasta] = score
    return scores


def _aplicar_exclusao_semantica(scores: dict, texto: str) -> dict:
    """
    V18 — Exclusão semântica baseada em contexto.

    Remove categorias cujo contexto indica domínio incompatível.
    Exemplo: se o texto contém "heart valve" ou "cardiac valve",
    a categoria raiz "Valves" (e todas as suas subpastas) é excluída,
    pois a patente é de domínio médico, não de engenharia mecânica.

    A exclusão é aplicada à categoria RAIZ: se "Valves" é excluída,
    "Valves/Check Valve", "Valves/Relief and Safety Valve" etc.
    também são excluídas.
    """
    if not _COMPILED_EXCLUSAO:
        return scores

    t = texto.lower()
    raizes_excluidas = set()

    for cat_raiz, padroes in _COMPILED_EXCLUSAO.items():
        for pat in padroes:
            if pat.search(t):
                raizes_excluidas.add(cat_raiz)
                break  # um hit basta para excluir a raiz

    if not raizes_excluidas:
        return scores

    return {
        pasta: score for pasta, score in scores.items()
        if pasta.split("/")[0] not in raizes_excluidas
    }


def _aplicar_preferencia_hierarquica(scores: dict) -> dict:
    """
    CORREÇÃO 2 — Remove pastas pai quando uma subpasta filha tem score.

    Regra: se "Valves" e "Valves/Check Valve" ambas têm score acima do
    mínimo, "Valves" é suprimida. A subpasta mais específica vence.

    Cascata: se "A", "A/B" e "A/B/C" têm score, apenas "A/B/C" fica.
    """
    filtrado = dict(scores)
    pastas_com_score = set(scores.keys())

    for pasta in list(filtrado.keys()):
        tem_descendente = any(
            outra.startswith(pasta + "/")
            for outra in pastas_com_score
            if outra != pasta
        )
        if tem_descendente:
            filtrado.pop(pasta, None)

    return filtrado


def _aplicar_prioridade_titulo(scores: dict, titulo: str) -> dict:
    """
    V19 — Prioridade por título.

    Se o TÍTULO da patente contém um termo-chave de domínio (ex: "pump",
    "bearing", "crusher"), dá prioridade às categorias desse domínio.

    Problema resolvido: uma patente intitulada "Needle Bearing" era
    classificada em "Sealings/Seal Ring and Gasket" porque o abstract
    mencionava "seal ring" como componente. Com esta regra, a categoria
    "Bearings/*" vence sobre "Sealings/*" quando o título contém "bearing".

    Regras:
    1. Só activa quando há conflito (scores em 2+ raízes diferentes)
    2. Mantém TODAS as categorias do domínio prioritário
    3. Remove categorias de outros domínios APENAS se o prioritário
       tiver score suficiente (não remove se o domínio do título
       tem score muito baixo comparado aos outros)
    """
    if not PRIORIDADE_TITULO or not scores:
        return scores

    titulo_lower = titulo.lower()

    # Encontrar domínios prioritários pelo título
    raizes_prioritarias = set()
    for termo, raizes in PRIORIDADE_TITULO.items():
        if termo in titulo_lower:
            raizes_prioritarias.update(raizes)

    if not raizes_prioritarias:
        return scores

    # Verificar se há conflito real (scores em raízes diferentes)
    raizes_com_score = set(p.split("/")[0] for p in scores)
    raizes_prio_com_score = raizes_prioritarias & raizes_com_score
    raizes_outras = raizes_com_score - raizes_prioritarias

    if not raizes_prio_com_score or not raizes_outras:
        return scores  # sem conflito

    # Calcular score máximo do domínio prioritário vs outros
    max_prio = max(
        (s for p, s in scores.items() if p.split("/")[0] in raizes_prioritarias),
        default=0
    )
    max_outro = max(
        (s for p, s in scores.items() if p.split("/")[0] not in raizes_prioritarias),
        default=0
    )

    # Só aplicar se o domínio prioritário tem score razoável
    # (pelo menos 50% do score do outro domínio)
    if max_prio < max_outro * 0.5:
        return scores  # score do domínio do título é muito fraco

    # Remover categorias de domínios não-prioritários
    return {
        p: s for p, s in scores.items()
        if p.split("/")[0] in raizes_prioritarias
    }


def _score1_fallback(texto: str) -> tuple:
    """
    NOVA REGRA — Fallback Score-1 para subpastas (SCORE_MINIMO=1).

    Activado apenas quando o fluxo principal não encontrou nenhuma pasta
    com score ≥ SCORE_MINIMO (= 2). Nesse caso:

      • Recalcula os scores com limiar = 1.
      • Aceita SOMENTE pastas que sejam subpastas (contêm "/"), nunca
        pastas raiz. Isso evita falsos positivos com termos ultra-genéricos
        como "valve" ou "pump" que existem na raiz.
      • Aplica exclusão semântica (V18) para evitar falsos positivos
        em domínios incompatíveis (ex: "heart valve" → não é Valves).
      • Se encontrar ao menos uma subpasta com score 1, classifica e
        adiciona o sufixo "(Confiança Baixa/Abstract Curto)" para
        sinalizar a baixa confiança no relatório.

    Retorna (p1, p2, p3, n_matches, status) ou None se nenhum match.
    """
    scores_raw = calcular_scores(texto, score_minimo=1)
    if not scores_raw:
        return None

    # V18: exclusão semântica também no fallback
    scores_raw = _aplicar_exclusao_semantica(scores_raw, texto)
    if not scores_raw:
        return None

    # Filtra: aceita apenas subpastas (com "/"), descarta raízes puras
    scores_sub = {p: s for p, s in scores_raw.items() if "/" in p}
    if not scores_sub:
        return None

    # V20: Bloquear categorias que viram "lixeira" no fallback score-1.
    # Estas categorias têm termos genéricos que matcham em qualquer patente
    # e só devem receber patentes com score >= 2 (match principal).
    _BLOQUEIO_FALLBACK = {
        "Manufacturing technology/Additive Manufacturing",
        "Sealings/Industrial Equipment Seals",
    }
    scores_sub = {p: s for p, s in scores_sub.items()
                  if p not in _BLOQUEIO_FALLBACK}
    if not scores_sub:
        return None

    # Aplica filtro hierárquico também aqui
    scores_filtrados = _aplicar_preferencia_hierarquica(scores_sub)
    if not scores_filtrados:
        scores_filtrados = scores_sub

    # Ordena: maior profundidade primeiro, score como desempate
    ordenados = sorted(
        scores_filtrados.items(),
        key=lambda kv: (-kv[0].count("/"), -kv[1])
    )

    destinos = [pasta + _SUFIXO_BAIXA_CONFIANCA for pasta, _ in ordenados]
    p1 = destinos[0] if len(destinos) > 0 else ""
    p2 = destinos[1] if len(destinos) > 1 else ""
    p3 = destinos[2] if len(destinos) > 2 else ""

    return p1, p2, p3, len(destinos), "Classificada (Confiança Baixa)"


def classificar(titulo: str, abstract: str) -> tuple:
    """
    Classifica uma patente pelo título + abstract.
    Retorna (p1, p2, p3, n_matches, status).

    Fluxo de classificação (3 correcções + 1 fallback + exclusão semântica):
      1. calcular_scores()                    → scoring ponderado (score ≥ 2)
      1b. _aplicar_exclusao_semantica()       → remove categorias fora de contexto
      2. _aplicar_preferencia_hierarquica()    → remove pastas pai
      3. Ordenação por profundidade desc, score desc
      4. _score1_fallback()                   → se passos 1-3 falharam,
                                                tenta score = 1 só em subpastas
    """
    _plac = {"não contém resumo", "não encontrado", "nan", "none", ""}

    resumo_limpo = abstract.strip()
    if resumo_limpo.lower() in _plac or resumo_limpo.lower().startswith("não contém"):
        resumo_limpo = ""

    texto = f"{titulo} {resumo_limpo}".strip()

    if not texto:
        return "", "", "", 0, "Sem abstract e título"

    sem_abstract = not resumo_limpo

    # ── Passo 1: scores com limiar normal (≥ 2) ──────────────────────
    scores = calcular_scores(texto)

    # ── Passo 1b: exclusão semântica (V18) ────────────────────────────
    scores = _aplicar_exclusao_semantica(scores, texto)

    # ── Passo 1c: prioridade por título (V19) ────────────────────────
    # Se o título indica "pump", "bearing", etc., prioriza o domínio
    # correspondente quando há conflito com menções secundárias.
    scores = _aplicar_prioridade_titulo(scores, titulo)

    if not scores:
        # ── Passo 4: Fallback Score-1 para subpastas ─────────────────
        # Activado quando: sem match com score ≥ 2.
        # Cobre abstracts curtos / títulos em PT sem abstract.
        resultado_fallback = _score1_fallback(texto)
        if resultado_fallback:
            return resultado_fallback

        status = "Sem match (abstract vazio)" if sem_abstract else "Sem match de palavras"
        return "", "", "", 0, status

    # ── Passo 2: filtro hierárquico ───────────────────────────────────
    scores_filtrados = _aplicar_preferencia_hierarquica(scores)
    if not scores_filtrados:
        scores_filtrados = scores  # fallback defensivo (hierarquia circular)

    # ── Passo 3: ordena — profundidade desc, score desc ───────────────
    #
    # ANTES: key=(-score, -profundidade) → raiz com muitos hits ganhava
    # AGORA: key=(-profundidade, -score) → subpasta específica vence
    ordenados = sorted(
        scores_filtrados.items(),
        key=lambda kv: (-kv[0].count("/"), -kv[1])
    )

    destinos = [pasta for pasta, _ in ordenados]
    p1 = destinos[0] if len(destinos) > 0 else ""
    p2 = destinos[1] if len(destinos) > 1 else ""
    p3 = destinos[2] if len(destinos) > 2 else ""

    return p1, p2, p3, len(destinos), "Classificada"


# ══════════════════════════════════════════════════════════════════════
# HELPERS DE CAMINHO
# ══════════════════════════════════════════════════════════════════════

def _nivel_pasta(pasta: str) -> int:
    """Retorna profundidade do caminho (0 = raiz, 1 = subpasta, ...)."""
    if not pasta:
        return -1
    return pasta.count("/")


def _pasta_raiz(pasta: str) -> str:
    return pasta.split("/")[0] if pasta else ""


def _pasta_nivel(pasta: str, nivel: int) -> str:
    partes = pasta.split("/")
    return "/".join(partes[:nivel + 1]) if len(partes) > nivel else pasta


# ══════════════════════════════════════════════════════════════════════
# FORMATAÇÃO EXCEL
# ══════════════════════════════════════════════════════════════════════

_FILL = {
    "Classificada":                    PatternFill("solid", fgColor="C6EFCE"),  # verde
    "Classificada (Confiança Baixa)":  PatternFill("solid", fgColor="D9E1F2"),  # azul claro
    "Sem match de palavras":           PatternFill("solid", fgColor="FFC7CE"),  # rosa
    "Sem abstract e título":           PatternFill("solid", fgColor="FFEB9C"),  # amarelo
    "Sem match (abstract vazio)":      PatternFill("solid", fgColor="FFEB9C"),  # amarelo
}
_FILL_HEADER   = PatternFill("solid", fgColor="1F4E79")
_FONT_HEADER   = Font(bold=True, color="FFFFFF", size=11)
_FONT_BOLD     = Font(bold=True)
_FONT_NORMAL   = Font(size=10)
_ALIGN_CENTER  = Alignment(horizontal="center", vertical="center", wrap_text=True)
_ALIGN_LEFT    = Alignment(horizontal="left",   vertical="center", wrap_text=True)
_BORDER_THIN   = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"),  bottom=Side(style="thin")
)
_LARGURAS = {
    "Código":           20,
    "Nome do Arquivo":  55,
    "Pasta Primária":   58,   # alargada para o sufixo "(Confiança Baixa/Abstract Curto)"
    "Pasta Secundária": 58,
    "Pasta Terciária":  58,
    "Status":           34,   # alargada para "Classificada (Confiança Baixa)"
}


def _aplicar_estilo_header(ws, n_cols):
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill      = _FILL_HEADER
        cell.font      = _FONT_HEADER
        cell.alignment = _ALIGN_CENTER
        cell.border    = _BORDER_THIN
    ws.row_dimensions[1].height = 28


def _aplicar_linha(ws, row_num, status, n_cols):
    fill = _FILL.get(status, PatternFill("solid", fgColor="FFFFFF"))
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=row_num, column=c)
        cell.fill      = fill
        cell.font      = _FONT_NORMAL
        cell.alignment = _ALIGN_LEFT
        cell.border    = _BORDER_THIN
    ws.cell(row=row_num, column=3).font = _FONT_BOLD


# ══════════════════════════════════════════════════════════════════════
# RELATÓRIO EM ÁRVORE NO TERMINAL
# ══════════════════════════════════════════════════════════════════════

def imprimir_arvore(contagem_p1, contagem_p2, contagem_p3, sem_classe):
    sep = "═" * 66

    raizes: dict = defaultdict(lambda: {"total": 0, "filhas": defaultdict(
        lambda: {"total": 0, "filhas": defaultdict(int)}
    )})

    for pasta, qtd in contagem_p1.items():
        raiz  = _pasta_raiz(pasta)
        nivel = _nivel_pasta(pasta)
        if nivel == 0:
            raizes[raiz]["total"] += qtd
        elif nivel == 1:
            raizes[raiz]["total"] += qtd
            raizes[raiz]["filhas"][pasta]["total"] += qtd
        else:
            raiz2 = _pasta_nivel(pasta, 1)
            raizes[raiz]["total"] += qtd
            raizes[raiz]["filhas"][raiz2]["total"] += qtd
            raizes[raiz]["filhas"][raiz2]["filhas"][pasta] += qtd

    print(f"\n{sep}")
    print("  DISTRIBUIÇÃO HIERÁRQUICA — PASTAS PRIMÁRIAS")
    print(sep)

    for raiz in sorted(raizes):
        info = raizes[raiz]
        print(f"\n  📁 {raiz}  ({info['total']} patente(s))")
        filhas_list = sorted(info["filhas"])
        for i, f2 in enumerate(filhas_list):
            conector = "└─" if i == len(filhas_list) - 1 else "├─"
            sub_info = info["filhas"][f2]
            print(f"       {conector} {f2.split('/')[-1]}  ({sub_info['total']})")
            sub_filhas_list = sorted(sub_info["filhas"])
            prefixo = "   " if i == len(filhas_list) - 1 else "│  "
            for j, f3 in enumerate(sub_filhas_list):
                con3 = "└─" if j == len(sub_filhas_list) - 1 else "├─"
                print(f"       {prefixo}    {con3} {f3.split('/')[-1]}  ({sub_info['filhas'][f3]})")

    if sem_classe:
        print(f"\n  ⚠  SEM CLASSIFICAÇÃO: {len(sem_classe)} patente(s)")

    print(f"\n{sep}")
    print("  RESUMO POR NÍVEL DE ESPECIFICIDADE")
    print(sep)

    # Remove o sufixo de confiança baixa antes de calcular nível
    def _pasta_sem_sufixo(p: str) -> str:
        return p.replace(_SUFIXO_BAIXA_CONFIANCA, "")

    so_raiz    = sum(q for p, q in contagem_p1.items() if _nivel_pasta(_pasta_sem_sufixo(p)) == 0)
    em_sub     = sum(q for p, q in contagem_p1.items() if _nivel_pasta(_pasta_sem_sufixo(p)) == 1)
    em_sub_sub = sum(q for p, q in contagem_p1.items() if _nivel_pasta(_pasta_sem_sufixo(p)) >= 2)
    total_class = so_raiz + em_sub + em_sub_sub

    # Conta separadamente as de baixa confiança (fallback score-1)
    bc = sum(q for p, q in contagem_p1.items() if _SUFIXO_BAIXA_CONFIANCA in p)

    print(f"  Pasta raiz (nível 1) apenas   : {so_raiz:>5}")
    print(f"  Subpasta   (nível 2)          : {em_sub:>5}")
    print(f"  Sub-subpasta (nível 3+)       : {em_sub_sub:>5}")
    print(f"  ─ dos quais Confiança Baixa   : {bc:>5}  ← fallback score-1")
    print(f"  Total classificadas           : {total_class:>5}")
    print(f"  Sem classificação             : {len(sem_classe):>5}")
    print(f"  TOTAL GERAL                   : {total_class + len(sem_classe):>5}")


# ══════════════════════════════════════════════════════════════════════
# PARTE C — TESTES DE REGRESSÃO
# ══════════════════════════════════════════════════════════════════════

# Abstracts realistas dos casos problemáticos documentados no diagnóstico
_CASOS_TESTE = [
    {
        "codigo":  "JP2023147990A",
        "titulo":  "Sleeve Valve",
        "abstract": (
            "A sleeve valve comprising a valve body with a sliding sleeve "
            "configured to control fluid flow. The sliding sleeve valve assembly "
            "includes a toe valve override mechanism for downhole completion "
            "operations. The interval control valve uses a production sleeve "
            "to manage inflow distribution across the wellbore."
        ),
        "p1_esperado": "Valves/Sleeve and Toe Valve",
        "p1_proibido": "Valves",
        "descricao": "Sleeve Valve → deve ir para Valves/Sleeve and Toe Valve (não raiz)",
    },
    {
        "codigo":  "CN205559274U",
        "titulo":  "External Relief Valve",
        "abstract": (
            "An external relief valve for controlling overpressure in fluid systems. "
            "The safety relief valve assembly includes a spring-loaded pressure "
            "relief mechanism. The bypass relief valve opens when system pressure "
            "exceeds the set pressure limiting valve threshold. Designed for use "
            "as an overpressure valve in twin screw pump installations."
        ),
        "p1_esperado": "Valves/Relief and Safety Valve",
        "p1_proibido": "Valves",
        "descricao": "External Relief Valve → deve ir para Valves/Relief and Safety Valve",
    },
    {
        "codigo":  "PI03013499",
        "titulo":  "Filtros Rotativos Vacuum",
        "abstract": (
            "Um sistema de filtro rotativo a vácuo composto por tambor rotativo "
            "com elemento de filtro resistente à corrosão para separação de "
            "sólidos. O setor de filtros rotativos aplica-se ao processamento "
            "de polpa de papel. O sistema de filtragem utiliza pressão de vácuo "
            "para drenar o líquido através da tela filtrante."
        ),
        "p1_esperado": None,        # não importa onde vai
        "p1_proibido": "Valves",    # mas NUNCA deve ir para Valves
        "descricao": "Filtros Rotativos → NÃO deve ir para Valves (Causa 3)",
    },
    {
        "codigo":  "JP7051484B2",
        "titulo":  "Check Valve Assembly",
        "abstract": (
            "A check valve assembly that prevents backflow in a fluid pipeline. "
            "The non-return valve includes a ball check valve mechanism with "
            "a one-way valve design. The backflow preventer incorporates a "
            "swing check valve for high-pressure pipeline applications."
        ),
        "p1_esperado": "Valves/Check Valve",
        "p1_proibido": "Valves",
        "descricao": "Check Valve → deve ir para Valves/Check Valve (não raiz)",
    },
    {
        "codigo":  "DE102015104300A1",
        "titulo":  "Screw Pump with Integrated Pressure Relief",
        "abstract": (
            "A screw pump with integrated pressure relief valve for overpressure "
            "protection. The relief valve screw pump includes a bypass relief valve "
            "that activates when pressure exceeds the pressure limiting valve "
            "threshold. The safety valve screw pump design integrates the relief "
            "mechanism directly into the pump body for compact installation."
        ),
        # Esta patente é legitimamente sobre bomba de parafuso E válvula de alívio.
        # Pumps/Screw Pump/Relief Valve é igualmente correto como P1.
        # O teste verifica que NÃO foi para a raiz pura "Valves".
        "p1_esperado": None,   # aceita qualquer subpasta específica
        "p1_proibido": "Valves",
        "descricao": "Relief Valve Screw Pump → subpasta específica (não raiz Valves)",
    },
    {
        "codigo":  "BACK_PRESSURE_TEST",
        "titulo":  "Back Pressure Valve",
        "abstract": (
            "A back pressure valve designed to maintain constant upstream pressure "
            "in fluid systems. The backpressure valve assembly includes a spring "
            "mechanism that prevents back-pressure valve fluctuations. Used as a "
            "bypass back valve in screw pump discharge lines and as a "
            "válvula de contrapressão in Brazilian petroleum applications."
        ),
        "p1_esperado": "Valves/Back Pressure Valve",
        "p1_proibido": "Valves",
        "descricao": "Back Pressure Valve → deve ir para Valves/Back Pressure Valve (nova subpasta)",
    },
    {
        "codigo":  "CONTROL_VALVE_PT",
        "titulo":  "Válvula de Controle de Capacidade",
        "abstract": (
            "Uma válvula de controle de deslocamento variável para sistemas "
            "de compressão. O dispositivo inclui válvula de controle de capacidade "
            "e válvula de controle de vazão para regulação precisa do fluxo. "
            "A válvula de controle proporcional opera via sinal eletropneumático."
        ),
        "p1_esperado": "Valves/Control and Flow Valve",
        "p1_proibido": "Valves",
        "descricao": "Válvula de Controle (PT) → deve ir para Valves/Control and Flow Valve (Causa 2)",
    },
    {
        "codigo":  "CHECK_VALVE_PT",
        "titulo":  "Válvula Antirretorno",
        "abstract": (
            "Uma válvula antirretorno para prevenir refluxo em tubulações industriais. "
            "A válvula de retenção inclui um mecanismo de disco oscilante que permite "
            "apenas o fluxo unidirecional. O projeto da válvula antirretorno de esfera "
            "oferece vedação confiável em sistemas de bombeamento."
        ),
        "p1_esperado": "Valves/Check Valve",
        "p1_proibido": "Valves",
        "descricao": "Válvula Antirretorno (PT) → deve ir para Valves/Check Valve (Causa 2)",
    },
]


def executar_testes_regressao(verbose: bool = True) -> dict:
    """
    Executa todos os casos de teste e retorna {codigo: resultado}.
    Se verbose=True, imprime relatório detalhado no terminal.
    """
    sep = "─" * 66
    resultados = {}
    aprovados = reprovados = 0

    if verbose:
        print(f"\n{'═'*66}")
        print("  PARTE C — TESTES DE REGRESSÃO")
        print(f"{'═'*66}")

    for caso in _CASOS_TESTE:
        p1, p2, p3, n, status = classificar(caso["titulo"], caso["abstract"])

        passou  = True
        motivos = []

        if caso["p1_esperado"] and caso["p1_esperado"] not in p1:
            passou = False
            motivos.append(f"P1='{p1}' ≠ esperado '{caso['p1_esperado']}'")

        if caso["p1_proibido"] and p1 == caso["p1_proibido"]:
            passou = False
            motivos.append(f"P1='{p1}' está na pasta proibida '{caso['p1_proibido']}'")

        icone = "✔" if passou else "✖"
        if passou:
            aprovados += 1
        else:
            reprovados += 1

        resultados[caso["codigo"]] = {
            "passou":  passou,
            "p1":      p1,
            "p2":      p2,
            "p3":      p3,
            "status":  status,
            "motivo":  "; ".join(motivos) if motivos else "OK",
        }

        if verbose:
            print(f"\n  {icone} [{caso['codigo']}]")
            print(f"     Desc : {caso['descricao']}")
            print(f"     P1   : {p1 or '(sem classificação)'}")
            print(f"     P2   : {p2 or '-'}")
            if not passou:
                for m in motivos:
                    print(f"     ⚠    {m}")

    if verbose:
        print(f"\n{'═'*66}")
        total = len(_CASOS_TESTE)
        print(f"  Resultado: {aprovados}/{total} aprovados", end="")
        if reprovados:
            print(f"  |  ⚠ {reprovados} REPROVADO(S) — verifique palavras_chave.py")
        else:
            print("  |  ✔ TODOS APROVADOS")
        print(f"{'═'*66}\n")

    return resultados


# ══════════════════════════════════════════════════════════════════════
# PARTE C — RELATÓRIO ANTES/DEPOIS (algoritmo antigo vs novo)
# ══════════════════════════════════════════════════════════════════════

def _calcular_scores_antigo(texto: str) -> dict:
    """
    Reimplementa o scoring ANTIGO (flat, sem ponderação) para comparação.
    Usado apenas pelo relatório --comparar; não afeta a classificação normal.
    """
    t = texto.lower()
    scores = {}
    for pasta, entradas in _COMPILED.items():
        hits = sum(1 for _, pat, _ in entradas if pat.search(t))
        if hits >= SCORE_MINIMO:
            scores[pasta] = hits
    return scores


def _classificar_antigo(titulo: str, abstract: str) -> str:
    """Classifica com o algoritmo ANTIGO e retorna apenas P1."""
    _plac = {"não contém resumo", "não encontrado", "nan", "none", ""}
    resumo = abstract.strip()
    if resumo.lower() in _plac:
        resumo = ""
    texto = f"{titulo} {resumo}".strip()
    if not texto:
        return ""
    scores = _calcular_scores_antigo(texto)
    if not scores:
        return ""
    return sorted(scores.items(), key=lambda kv: (-kv[1], -kv[0].count("/")))[0][0]


def comparar_algoritmos(excel_path: str) -> None:
    """
    Parte C — Relatório antes/depois sobre a planilha real.
    Mostra quantas patentes ficam na raiz vs subpastas em cada algoritmo
    e lista as patentes que "migraram" de raiz para subpasta.
    """
    sep = "═" * 66

    if not os.path.exists(excel_path):
        print(f"\n  ✖ Planilha não encontrada: {excel_path}")
        return

    df = pd.read_excel(excel_path, engine="openpyxl")
    n = len(df)

    print(f"\n{sep}")
    print("  PARTE C — RELATÓRIO ANTES/DEPOIS")
    print(f"  Planilha : {excel_path}")
    print(f"  Patentes : {n}")
    print(sep)

    ant_raiz = ant_sub = ant_sub_sub = ant_sem = 0
    nov_raiz = nov_sub = nov_sub_sub = nov_sem = 0
    migrados_raiz_sub   = []   # raiz → subpasta (melhoria)
    migrados_sub_raiz   = []   # subpasta → raiz (regressão)

    for _, row in df.iterrows():
        codigo   = str(row.get("Código",   "") or "").strip()
        titulo   = str(row.get("Título",   "") or "").strip()
        abstract = str(row.get("Abstract", "") or "").strip()

        p1_ant = _classificar_antigo(titulo, abstract)
        p1_nov, _, _, _, _ = classificar(titulo, abstract)

        niv_ant = _nivel_pasta(p1_ant)
        niv_nov = _nivel_pasta(p1_nov)

        if not p1_ant:     ant_sem    += 1
        elif niv_ant == 0: ant_raiz   += 1
        elif niv_ant == 1: ant_sub    += 1
        else:              ant_sub_sub += 1

        if not p1_nov:     nov_sem    += 1
        elif niv_nov == 0: nov_raiz   += 1
        elif niv_nov == 1: nov_sub    += 1
        else:              nov_sub_sub += 1

        # Detecta migrações relevantes
        if p1_ant and niv_ant == 0 and p1_nov and niv_nov >= 1:
            migrados_raiz_sub.append((codigo, p1_ant, p1_nov))
        elif p1_ant and niv_ant >= 1 and p1_nov and niv_nov == 0:
            migrados_sub_raiz.append((codigo, p1_ant, p1_nov))

    # Tabela resumo
    print(f"\n  {'Categoria':<38} {'ANTES':>7} {'DEPOIS':>7} {'Δ':>7}")
    print(f"  {'─'*38} {'─'*7} {'─'*7} {'─'*7}")

    def _linha(label, ant, dep):
        delta = dep - ant
        sinal = f"+{delta}" if delta > 0 else str(delta)
        print(f"  {label:<38} {ant:>7} {dep:>7} {sinal:>7}")

    _linha("Na pasta raiz apenas (nível 1)",   ant_raiz,    nov_raiz)
    _linha("Em subpasta (nível 2)",             ant_sub,     nov_sub)
    _linha("Em sub-subpasta (nível 3+)",        ant_sub_sub, nov_sub_sub)
    _linha("Sem classificação",                 ant_sem,     nov_sem)
    print(f"  {'─'*38} {'─'*7} {'─'*7} {'─'*7}")
    _linha("TOTAL",                             n,           n)

    # Migrações raiz → subpasta (melhorias)
    if migrados_raiz_sub:
        print(f"\n  ✔ Patentes migradas de raiz → subpasta ({len(migrados_raiz_sub)})")
        for cod, ant, novo in migrados_raiz_sub[:20]:
            print(f"    [{cod:<20}]  {ant:<15}  →  {novo}")
        if len(migrados_raiz_sub) > 20:
            print(f"    ... e mais {len(migrados_raiz_sub) - 20} patente(s)")

    # Regressões subpasta → raiz (alertas)
    if migrados_sub_raiz:
        print(f"\n  ⚠ Patentes que regrediram subpasta → raiz ({len(migrados_sub_raiz)})")
        for cod, ant, novo in migrados_sub_raiz:
            print(f"    [{cod:<20}]  {ant:<30}  →  {novo}")
        print("    (Verifique se os termos dessas subpastas foram removidos por engano)")

    print(f"\n{sep}\n")


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Auditoria de classificação de patentes (somente leitura)"
    )
    parser.add_argument("--excel",    default=EXCEL_FILE,
                        help="Planilha principal de patentes")
    parser.add_argument("--saida",    default=SAIDA_FILE,
                        help="Planilha de saída do relatório")
    parser.add_argument("--testes",   action="store_true",
                        help="Executa apenas os testes de regressão e sai")
    parser.add_argument("--comparar", action="store_true",
                        help="Exibe relatório antes/depois do algoritmo e sai")
    args = parser.parse_args()

    sep = "═" * 66
    print(f"\n{sep}")
    print("  Auditoria de Classificação de Patentes")
    print("  (modo somente leitura — nenhum arquivo é alterado)")
    print(sep)

    # ── Modo: apenas testes de regressão ─────────────────────────────
    if args.testes:
        executar_testes_regressao(verbose=True)
        return

    # ── Modo: relatório antes/depois ──────────────────────────────────
    if args.comparar:
        comparar_algoritmos(args.excel)
        return

    # ── Verifica planilha ─────────────────────────────────────────────
    if not os.path.exists(args.excel):
        print(f"\n  ✖ Planilha não encontrada: {args.excel}")
        raise SystemExit(1)

    # Sempre executa os testes antes de classificar — alerta precoce
    print("\n  Verificando regressões antes de gerar o relatório...")
    resultados_teste = executar_testes_regressao(verbose=False)
    n_reprovados = sum(1 for r in resultados_teste.values() if not r["passou"])
    if n_reprovados:
        print(f"  ⚠  {n_reprovados} teste(s) de regressão falharam.")
        print("     Use --testes para ver detalhes. Prosseguindo mesmo assim...\n")
    else:
        print(f"  ✔ {len(resultados_teste)} testes de regressão passaram\n")

    # ── Lê planilha ───────────────────────────────────────────────────
    print(f"  Lendo: {args.excel}")
    df = pd.read_excel(args.excel, engine="openpyxl")
    n_total = len(df)
    print(f"  Patentes carregadas: {n_total}\n")

    # ── Classifica ────────────────────────────────────────────────────
    registros  = []
    contagem_p1 = defaultdict(int)
    contagem_p2 = defaultdict(int)
    contagem_p3 = defaultdict(int)
    sem_classe  = []

    for _, row in df.iterrows():
        codigo   = str(row.get("Código",          "") or "").strip()
        nome_arq = str(row.get("Nome do Arquivo",  "") or "").strip()
        titulo   = str(row.get("Título",           "") or "").strip()
        abstract = str(row.get("Abstract",         "") or "").strip()

        p1, p2, p3, n_matches, status = classificar(titulo, abstract)

        if p1: contagem_p1[p1] += 1
        if p2: contagem_p2[p2] += 1
        if p3: contagem_p3[p3] += 1
        if not p1: sem_classe.append(codigo)

        registros.append({
            "Código":           codigo,
            "Nome do Arquivo":  nome_arq,
            "Pasta Primária":   p1,
            "Pasta Secundária": p2,
            "Pasta Terciária":  p3,
            "Status":           status,
        })

        if len(registros) % 50 == 0:
            print(f"  ... {len(registros)}/{n_total} processadas")

    print(f"  {n_total}/{n_total} processadas.\n")

    # ── Gera DataFrame de saída ───────────────────────────────────────
    df_out = pd.DataFrame(registros, columns=[
        "Código", "Nome do Arquivo",
        "Pasta Primária", "Pasta Secundária", "Pasta Terciária", "Status"
    ])

    # ── Salva Excel ───────────────────────────────────────────────────
    print(f"  Gerando planilha: {args.saida}")
    df_out.to_excel(args.saida, index=False, engine="openpyxl")

    wb = load_workbook(args.saida)
    ws = wb.active
    ws.title = "Auditoria"
    n_cols   = len(df_out.columns)

    _aplicar_estilo_header(ws, n_cols)

    for i, col_name in enumerate(df_out.columns, start=1):
        largura = _LARGURAS.get(col_name, 20)
        ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = largura

    ws.freeze_panes = "A2"

    for row_num, reg in enumerate(registros, start=2):
        _aplicar_linha(ws, row_num, reg["Status"], n_cols)

    # ── Aba de resumo por pasta ───────────────────────────────────────
    ws_res = wb.create_sheet("Resumo por Pasta")
    cabecalhos_res = [
        "Pasta", "Nível",
        "Patentes (Primária)", "Patentes (Secundária)", "Patentes (Terciária)"
    ]
    ws_res.append(cabecalhos_res)

    for c in range(1, len(cabecalhos_res) + 1):
        cell = ws_res.cell(row=1, column=c)
        cell.fill      = _FILL_HEADER
        cell.font      = _FONT_HEADER
        cell.alignment = _ALIGN_CENTER
        cell.border    = _BORDER_THIN

    ws_res.column_dimensions["A"].width = 55
    ws_res.column_dimensions["B"].width = 10
    ws_res.column_dimensions["C"].width = 22
    ws_res.column_dimensions["D"].width = 22
    ws_res.column_dimensions["E"].width = 22

    todas_pastas = set(contagem_p1) | set(contagem_p2) | set(contagem_p3)
    for pasta in sorted(todas_pastas):
        nivel = _nivel_pasta(pasta) + 1
        ws_res.append([
            pasta, nivel,
            contagem_p1.get(pasta, 0),
            contagem_p2.get(pasta, 0),
            contagem_p3.get(pasta, 0),
        ])
        r = ws_res.max_row
        for c in range(1, len(cabecalhos_res) + 1):
            cell = ws_res.cell(row=r, column=c)
            cell.border    = _BORDER_THIN
            cell.alignment = _ALIGN_LEFT
            cell.font      = _FONT_NORMAL
        ws_res.cell(row=r, column=1).value = (
            "    " * _nivel_pasta(pasta)
        ) + pasta.split("/")[-1]

    ws_res.freeze_panes = "A2"
    ws_res.auto_filter.ref = f"A1:E{ws_res.max_row}"
    ws.auto_filter.ref = f"A1:F{len(registros)+1}"

    wb.save(args.saida)
    print("  ✔ Planilha salva com sucesso.")

    # ── Relatório em árvore no terminal ───────────────────────────────
    imprimir_arvore(contagem_p1, contagem_p2, contagem_p3, sem_classe)

    print(f"\n{sep}")
    print(f"  Relatório completo: {args.saida}")
    print(sep + "\n")


if __name__ == "__main__":
    main()
