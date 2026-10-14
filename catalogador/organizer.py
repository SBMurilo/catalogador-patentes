# ============================================================
#  organizer.py — Organização Final dos PDFs
# ============================================================
#
#  Para cada CODIGO.pdf em Patentes_Codigo:
#    - Código encontrado na planilha  → renomeia para CódigoPesquisado_CurrentAssignee_Título.pdf
#                                       atualiza "Nome do Arquivo" na planilha
#                                       move para PASTA_DESTINO (Patentes)
#    - Código não encontrado          → move para PASTA_SEM (Revisao)
#
# ============================================================

import os
import re
import sys
import shutil

import pandas as pd

from config import EXCEL_FILE, PASTA_CODIGO, PASTA_SEM, PASTA_DESTINO


def _long_path(path):
    r"""Adiciona prefixo \\?\ no Windows para suportar caminhos > 260 caracteres."""
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


# Limite seguro para o nome do arquivo (sem extensão)
_MAX_NOME = 180


def _truncar_nome(nome):
    """Trunca o nome do arquivo se ultrapassar _MAX_NOME caracteres."""
    if len(nome) <= _MAX_NOME:
        return nome
    return nome[:_MAX_NOME]


def _limpar_nome(texto):
    """Remove caracteres inválidos para nome de arquivo, preservando letras acentuadas."""
    import unicodedata
    sem_acento = unicodedata.normalize('NFKD', str(texto)).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^A-Za-z0-9]', '', sem_acento)


def run_organizer():
    """Organiza os PDFs de Patentes_Codigo usando os dados da planilha."""

    # --- Verificações iniciais ---
    if not os.path.exists(EXCEL_FILE):
        print(f"ERRO: Planilha não encontrada: {EXCEL_FILE}")
        print("Execute a catalogação (opções 1, 2 ou 3) antes de organizar.")
        return

    if not os.path.exists(PASTA_CODIGO):
        print(f"ERRO: Pasta não encontrada: {PASTA_CODIGO}")
        return

    os.makedirs(PASTA_DESTINO, exist_ok=True)
    os.makedirs(PASTA_SEM, exist_ok=True)

    # --- Carregar planilha ---
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')

    # Índice rápido: tanto Código quanto Código Pesquisado apontam para a mesma linha.
    # Isso resolve o caso onde o arquivo em Patentes_Codigo tem nome canônico (ex: JP7051484B2.pdf)
    # mas o Excel registrou o código original com zeros (ex: JP007051484B2).
    indice = {}
    for idx, row in df.iterrows():
        cod_original  = str(row["Código"]).strip()
        cod_pesquisado = str(row.get("Código Pesquisado", "")).strip()
        indice[cod_original] = idx
        if cod_pesquisado and cod_pesquisado != cod_original:
            indice[cod_pesquisado] = idx

    # --- Listar PDFs em Patentes_Codigo ---
    arquivos = [f for f in os.listdir(PASTA_CODIGO) if f.lower().endswith(".pdf")]

    if not arquivos:
        print("Pasta Patentes_Codigo está vazia. Nada para organizar.")
        return

    total         = len(arquivos)
    contador_ok   = 0
    contador_sem  = 0
    planilha_atualizada = False

    print(f"\n{total} arquivo(s) encontrado(s) em Patentes_Codigo...\n")

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_CODIGO, arquivo)
        codigo  = os.path.splitext(arquivo)[0].upper()  # CODIGO.pdf → CODIGO

        # --- Não encontrado na planilha → Revisao ---
        if codigo not in indice:
            destino = os.path.join(PASTA_SEM, arquivo)
            # garantir nome único em Revisao
            if os.path.exists(_long_path(destino)):
                base, ext = os.path.splitext(arquivo)
                c = 1
                while os.path.exists(_long_path(destino)):
                    destino = os.path.join(PASTA_SEM, f"{base}_{c}{ext}")
                    c += 1
            _mover(caminho, destino)
            print(f"  [SEM INFO]   {arquivo}  →  Revisao/")
            contador_sem += 1
            continue

        # --- Encontrado na planilha → renomeia e move para Patentes ---
        idx = indice[codigo]
        row = df.loc[idx]

        codigo_pesquisado = _limpar_nome(row.get("Código Pesquisado", codigo))
        current_assignee  = _limpar_nome(row.get("Current Assignee", ""))
        titulo            = _limpar_nome(row.get("Título", ""))

        novo_nome_base = _truncar_nome(f"{codigo_pesquisado}_{current_assignee}_{titulo}")
        novo_nome_pdf  = f"{novo_nome_base}.pdf"

        # garantir nome único em Patentes
        destino = os.path.join(PASTA_DESTINO, novo_nome_pdf)
        if os.path.exists(_long_path(destino)):
            c = 1
            while os.path.exists(_long_path(destino)):
                destino = os.path.join(PASTA_DESTINO, f"{novo_nome_base}_{c}.pdf")
                c += 1

        _mover(caminho, destino)

        # Atualizar coluna "Nome do Arquivo" na planilha
        df.at[idx, "Nome do Arquivo"] = novo_nome_base
        planilha_atualizada = True

        print(f"  [OK]         {arquivo}  →  Patentes/{novo_nome_pdf}")
        contador_ok += 1

    # --- Salvar planilha se houve mudanças ---
    if planilha_atualizada:
        df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
        print(f"\nPlanilha '{EXCEL_FILE}' atualizada com os novos nomes.")

    print("\n============================")
    print("Organização finalizada")
    print("============================")
    print(f"  Organizados:   {contador_ok}")
    print(f"  Sem info:      {contador_sem}")
    print(f"  Total:         {total}")
