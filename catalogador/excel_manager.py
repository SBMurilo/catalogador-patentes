# ============================================================
#  excel_manager.py — Gerenciamento dos Arquivos Excel
# ============================================================

import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

from config import EXCEL_FILE, REVIEW_FILE


def save_to_excel(data_row, excel_file, data_not_extracted):
    """Salva os dados e aplica cor se os dados não foram extraídos com sucesso."""
    df_new = pd.DataFrame([data_row])
    if not os.path.exists(excel_file):
        df_new.to_excel(excel_file, index=False, engine='openpyxl')
    else:
        df_existing = pd.read_excel(excel_file, engine='openpyxl')
        pd.concat([df_existing, df_new], ignore_index=True).to_excel(
            excel_file, index=False, engine='openpyxl'
        )

    if data_not_extracted:
        wb = load_workbook(excel_file)
        ws = wb.active
        red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        for col in range(1, ws.max_column + 1):
            ws.cell(row=ws.max_row, column=col).fill = red_fill
        wb.save(excel_file)


def save_to_review(data_row, review_file=REVIEW_FILE, status=None):
    """
    Salva patentes na planilha de revisão.
    status: mensagem para coluna 'Status' (ex: 'Não encontrado', 'Download não disponível')
    Se status for informado, a linha receberá essa descrição na coluna Status.
    """
    row = dict(data_row)
    if status is not None:
        row["Status"] = status
        # Preserva Título e dados para "Download nao disponivel" — necessário para
        # migração posterior para planilha principal quando o PDF for adicionado.
        # Para "Nao encontrado" não há dados úteis, então limpa.
        if status != "Download nao disponivel":
            row["Título"] = ""
            row["Nome do Arquivo"] = ""

    df_new = pd.DataFrame([row])
    if not os.path.exists(review_file):
        df_new.to_excel(review_file, index=False, engine='openpyxl')
    else:
        df_existing = pd.read_excel(review_file, engine='openpyxl')
        # Garantir que coluna Status exista em ambos
        if "Status" not in df_existing.columns:
            df_existing["Status"] = ""
        if "Status" not in df_new.columns:
            df_new["Status"] = ""
        pd.concat([df_existing, df_new], ignore_index=True).to_excel(
            review_file, index=False, engine='openpyxl'
        )
    
    # Pintar linha de amarelo para diferenciar de "vermelho = erro de scraping"
    if status is not None:
        wb = load_workbook(review_file)
        ws = wb.active
        yellow_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        for col in range(1, ws.max_column + 1):
            ws.cell(row=ws.max_row, column=col).fill = yellow_fill
        wb.save(review_file)


def reprocess_review_file(driver, codes_in_folder, review_file=REVIEW_FILE, excel_file=EXCEL_FILE):
    """Tenta corrigir apenas patentes da revisão que possuem PDF na pasta."""
    # import aqui para evitar circular import
    from scraper import get_patent_data
    from utils import generate_review_variations

    if not os.path.exists(review_file):
        print("\nNenhuma planilha de revisão encontrada.")
        return

    print("\n--- Iniciando reprocessamento da revisão ---")

    df = pd.read_excel(review_file)
    indices_para_remover = []

    for idx, row in df.iterrows():
        original_code = str(row["Código"])

        # só tenta se o PDF existir na pasta
        if original_code not in codes_in_folder:
            continue

        variations = generate_review_variations(original_code)

        for new_code in variations:
            print(f"Tentando variação {new_code}")
            data, found = get_patent_data(driver, new_code)

            if found:
                print(f"Encontrado com código corrigido: {new_code}")
                data["Código"]           = original_code
                data["Código Pesquisado"] = new_code
                save_to_excel(data, excel_file, False)
                indices_para_remover.append(idx)
                break

    if indices_para_remover:
        df = df.drop(indices_para_remover)
        df.to_excel(review_file, index=False)
        print(f"{len(indices_para_remover)} patentes recuperadas da revisão.")
    else:
        print("Nenhuma patente recuperada.")


def load_processed_codes(excel_file=EXCEL_FILE, review_file=REVIEW_FILE):
    """Retorna o conjunto de códigos a serem pulados no processamento normal.
    Inclui:
      - Todos os códigos da planilha principal
      - Códigos da revisão com status 'Nao encontrado' (scraping já foi feito, nada achado)
    NÃO inclui códigos com 'Download nao disponivel' — esses têm dados e devem ser
    migrados para a planilha principal quando o PDF for adicionado."""
    codes = set()

    # Planilha principal — todos os códigos
    if os.path.exists(excel_file):
        try:
            df = pd.read_excel(excel_file, engine='openpyxl')
            codes.update(df["Código"].astype(str).tolist())
            if "Código Pesquisado" in df.columns:
                codes.update(df["Código Pesquisado"].dropna().astype(str).tolist())
        except Exception:
            pass

    # Planilha de revisão — apenas "Nao encontrado"
    if os.path.exists(review_file):
        try:
            df = pd.read_excel(review_file, engine='openpyxl')
            if "Status" in df.columns:
                nao_encontrados = df[df["Status"].astype(str) == "Nao encontrado"]
                codes.update(nao_encontrados["Código"].astype(str).tolist())
        except Exception:
            pass

    return codes


def load_review_codes_by_status(review_file=REVIEW_FILE):
    """Retorna dicionário {codigo: status} para todos os registros da planilha de revisão."""
    if not os.path.exists(review_file):
        return {}
    try:
        df = pd.read_excel(review_file, engine='openpyxl')
        if "Código" not in df.columns or "Status" not in df.columns:
            return {}
        return dict(zip(df["Código"].astype(str), df["Status"].astype(str)))
    except Exception:
        return {}


def load_main_codes(excel_file=EXCEL_FILE):
    """Retorna apenas os códigos da planilha principal (sem revisão)."""
    if not os.path.exists(excel_file):
        return set()
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        codes = set(df["Código"].astype(str).tolist())
        if "Código Pesquisado" in df.columns:
            codes.update(df["Código Pesquisado"].dropna().astype(str).tolist())
        return codes
    except Exception:
        return set()


def mover_revisao_para_principal(codigo, review_file=REVIEW_FILE, excel_file=EXCEL_FILE):
    """Move uma patente da planilha de revisão para a planilha principal.
    Usado quando o PDF de uma patente 'Download nao disponivel' é adicionado posteriormente.
    Retorna True se a migração ocorreu com sucesso."""
    if not os.path.exists(review_file):
        return False
    try:
        df = pd.read_excel(review_file, engine='openpyxl')
        mask = df["Código"].astype(str) == str(codigo)
        if not mask.any():
            return False

        row = df[mask].iloc[0].to_dict()

        # Remove colunas que não existem na planilha principal
        row.pop("Status", None)

        # Garante que Nome do Arquivo não está em branco — gera se necessário
        if not str(row.get("Nome do Arquivo", "")).strip() or row.get("Nome do Arquivo") == "nan":
            from utils import gerar_nome_arquivo
            row["Nome do Arquivo"] = gerar_nome_arquivo(row)

        save_to_excel(row, excel_file, False)

        # Remove da revisão
        df = df[~mask]
        df.to_excel(review_file, index=False, engine='openpyxl')

        return True
    except Exception as e:
        print(f"  Erro ao migrar {codigo} da revisão: {e}")
        return False
