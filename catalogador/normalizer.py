# ============================================================
#  normalizer.py — Normalização de PDFs da pasta Inserir
# ============================================================

import os
import re
import sys
import shutil

from config import PASTA_INSERIR, PASTA_CODIGO, PASTA_SEM, PASTA_LIXO


# Padrão de código de patente (suporta prefixos de 2 ou 3 letras: JP, US, JPH, JPS, etc.)
PADRAO = re.compile(r'[A-Z]{2,3}\d{4,}[A-Z0-9]*', re.I)


def _long_path(path):
    """
    No Windows, adiciona o prefixo \\\\?\\ para suportar caminhos longos (> 260 caracteres).
    Em outros sistemas operacionais, retorna o caminho sem alteração.
    """
    if sys.platform != "win32":
        return path
    path = os.path.abspath(path)
    if path.startswith("\\\\?\\"):
        return path
    if path.startswith("\\\\"):
        # Caminho UNC: \\servidor\share → \\?\UNC\servidor\share
        return "\\\\?\\UNC\\" + path[2:]
    return "\\\\?\\" + path


def extrair_codigo(nome):
    """Extrai código de patente do nome do arquivo.
    Se o código terminar com letra duplicada (ex: AA, BB), remove a última.
    Ex: JP002000009050AA → JP002000009050A
    """
    resultado = PADRAO.search(nome.upper())
    if not resultado:
        return None
    codigo = resultado.group(0)
    # Remove sufixo duplicado: se termina em XY e X == Y (ex: AA, BB), fica só X
    if len(codigo) >= 2 and codigo[-1].isalpha() and codigo[-2] == codigo[-1]:
        codigo = codigo[:-1]
    return codigo


def _destino_unico(pasta, nome_arquivo):
    """Garante nome de arquivo único na pasta destino."""
    destino = os.path.join(pasta, nome_arquivo)
    if not os.path.exists(_long_path(destino)):
        return destino
    base, ext = os.path.splitext(nome_arquivo)
    contador = 1
    while True:
        novo = os.path.join(pasta, f"{base}_{contador}{ext}")
        if not os.path.exists(_long_path(novo)):
            return novo
        contador += 1


def _mover(origem, destino):
    """Move arquivo usando caminhos longos no Windows."""
    shutil.move(_long_path(origem), _long_path(destino))


def run_normalizer(processed_codes: set = None):
    """
    Lê PDFs da pasta Inserir e os distribui:
      - Código reconhecido e arquivo ainda não em Patentes_Codigo → move e renomeia
      - Arquivo já existe em Patentes_Codigo (duplicata física)   → Lixo/
      - Sem código reconhecido                                     → Revisao/

    Obs: processed_codes não é usado aqui — a checagem é feita pelo arquivo
    físico em Patentes_Codigo, não pela planilha. Isso permite que PDFs
    baixados pelas opções 1/2 sejam normalizados corretamente.
    """

    pasta_info = str(PASTA_INSERIR)
    print("Pasta configurada: " + pasta_info)

    if not os.path.exists(_long_path(PASTA_INSERIR)):
        print("ERRO: Pasta nao encontrada! Verifique o caminho em config.py.")
        return

    todos = os.listdir(_long_path(PASTA_INSERIR))

    # Coleta todos os PDFs recursivamente (incluindo subpastas)
    arquivos_caminhos = []
    for raiz, _, files in os.walk(_long_path(PASTA_INSERIR)):
        for f in files:
            if f.lower().endswith(".pdf"):
                # Armazena o caminho sem o prefixo \\?\ para exibição legível
                caminho_completo = os.path.join(raiz, f)
                arquivos_caminhos.append(caminho_completo)

    print("Arquivos na pasta (total): " + str(len(todos)))
    print("PDFs encontrados:          " + str(len(arquivos_caminhos)))

    if not arquivos_caminhos:
        if todos:
            print("A pasta tem arquivos, mas nenhum .pdf foi encontrado (incluindo subpastas).")
        else:
            print("Pasta vazia. Coloque os PDFs em: " + pasta_info)
        return

    total        = len(arquivos_caminhos)
    contador_ok  = 0
    contador_dup = 0
    contador_sem = 0
    contador_err = 0

    print(f"\n{total} arquivo(s) encontrado(s) em Inserir (incluindo subpastas)...\n")

    for caminho in arquivos_caminhos:
        arquivo = os.path.basename(caminho)
        codigo  = extrair_codigo(arquivo)

        try:
            # --- Sem código: vai para Revisao com nome original
            if not codigo:
                destino = _destino_unico(PASTA_SEM, arquivo)
                _mover(caminho, destino)
                print(f"  [SEM CÓDIGO]  {arquivo}  →  Revisao/")
                contador_sem += 1
                continue

            codigo = codigo.upper()

            # --- Duplicata física: arquivo já existe em Patentes_Codigo → Lixo
            if os.path.exists(_long_path(os.path.join(PASTA_CODIGO, f"{codigo}.pdf"))):
                destino = _destino_unico(PASTA_LIXO, arquivo)
                _mover(caminho, destino)
                print(f"  [DUPLICADO]   {codigo}  →  Lixo/  (já existe em Patentes_Codigo)")
                contador_dup += 1
                continue

            # --- OK: renomeia para CODIGO.pdf e move para Patentes_Codigo
            destino = _destino_unico(PASTA_CODIGO, f"{codigo}.pdf")
            _mover(caminho, destino)
            print(f"  [OK]          {arquivo}  →  Patentes_Codigo/{codigo}.pdf")
            contador_ok += 1

        except Exception as e:
            print(f"  [ERRO]        {arquivo}  →  {e}")
            contador_err += 1

    print("\n============================")
    print("Normalização finalizada")
    print("============================")
    print(f"  Normalizados:  {contador_ok}")
    print(f"  Duplicados:    {contador_dup}")
    print(f"  Sem código:    {contador_sem}")
    if contador_err:
        print(f"  Erros:         {contador_err}")
    print(f"  Total:         {total}")
