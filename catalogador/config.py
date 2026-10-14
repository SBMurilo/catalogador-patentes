# ============================================================
#  config.py — Configurações Globais
# ============================================================

import os

# --- Arquivos Excel ---
# DEPOIS
EXCEL_FILE  = r"C:\Projetos\Testes_Prog_Patente\Projeto\patents_data_test.xlsx"
REVIEW_FILE = r"C:\Projetos\Testes_Prog_Patente\Projeto\patents_para_revisao.xlsx"

# --- Pastas do Sistema ---
PASTA_DESTINO = r"C:\Projetos\Testes_Prog_Patente\Projeto\Patentes"
PASTA_INSERIR = r"C:\Projetos\Testes_Prog_Patente\Projeto\Patentes\Inserir"         # PDFs brutos entram aqui
PASTA_CODIGO  = r"C:\Projetos\Testes_Prog_Patente\Projeto\Prog_Patente\Patentes_aux\Patentes_codigo"  # PDFs normalizados (codigo.pdf)
PASTA_SEM     = r"C:\Projetos\Testes_Prog_Patente\Projeto\Prog_Patente\Patentes_aux\Revisao"          # PDFs sem código reconhecido
PASTA_LIXO    = r"C:\Projetos\Testes_Prog_Patente\Projeto\Prog_Patente\Patentes_aux\Lixo"              # PDFs realmente duplicados

# Garante que todas as pastas existem ao importar o config
for _p in (PASTA_INSERIR, PASTA_CODIGO, PASTA_SEM, PASTA_LIXO):
    os.makedirs(_p, exist_ok=True)

TEST_PATENTS = [
    "DE202014010877U1",
    "DE202014010816U1",
    "DE202009002875U1",
    "ES2576732T3",
    "US2011151664A1",
    "US2013251581A1",
    "US2015251147A1",
    "US2016061200A1",
    "CN105840498A",
    "JP2015161307A",
    "DE102013101164A1",
    "DE102012002816A1",
    "DE102011101648A1",
    "DE102011101641A1",
    "DE102010044824A1",
    "DE102010005930A1",
    "EP2336590A2",
    "EP2322803A2",
    "DE102009019220A1",
    "DE102004002837A1",
    "DE10226501A1",
    "DE102015104300A1",
    "DE102014116779A1",
    "NL8203882A",
    "DE29921591U1",
    "DE29808800U1",
    "DE29715798U1",
    "DE29715797U1",
    "DE29710068U1",
    "DE29710066U1",
    "DE29710065U1",
    "DE29710064U1",
    "DE29600604U1",
    "DE29503636U1",
    "DE29503173U1",
    "DE29503172U1",
    "DE29501603U1",
    "DE29501602U1",
    "DE29501601U1",
    "DE29501600U1",
    "DE29501599U1",
    "DE29501598U1",
    "DE20000281U1",
    "DE9403275U1",
    "DE9315547U1",
    "DE9314746U1"
]