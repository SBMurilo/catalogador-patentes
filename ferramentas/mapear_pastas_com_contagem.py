"""
mapear_pastas_com_contagem.py
──────────────────────────────
Lê a hierarquia de pastas a partir de um diretório raiz e gera
um arquivo TXT com a árvore visual de pastas + total de arquivos
(considerando a pasta + todas as suas subpastas).

Como usar:
  1. Coloque este script em qualquer lugar
  2. Edite a variável PASTA_RAIZ abaixo com o caminho da sua pasta
  3. Execute: python mapear_pastas_com_contagem.py
  4. O arquivo de saída será gerado na mesma pasta do script
"""

import os
import pathlib

# ══════════════════════════════════════════════════════════════
# CONFIGURAÇÃO — edite apenas esta linha
# ══════════════════════════════════════════════════════════════
PASTA_RAIZ = r"C:\caminho\para\sua\pasta"   # ← edite aqui
# ══════════════════════════════════════════════════════════════

# Arquivo de saída (gerado na mesma pasta do script)
SCRIPT_DIR = pathlib.Path(__file__).parent
SAIDA_TXT  = SCRIPT_DIR / "hierarquia_pastas.txt"


# ── 1. Coleta a hierarquia de pastas com contagem de arquivos ─
def coletar_pastas(raiz: str) -> list[dict]:
    """
    Percorre a árvore de diretórios e retorna uma lista de dicts:
      {
        'caminho'   : Path,
        'nome'      : str,
        'nivel'     : int,
        'arq_total' : int,   # arquivos na pasta + todas as subpastas
      }
    """
    raiz_path = pathlib.Path(raiz)
    if not raiz_path.exists():
        print(f"\n  ✖ Pasta não encontrada: {raiz}")
        print("  Edite a variável PASTA_RAIZ no início do script.\n")
        raise SystemExit(1)

    # Primeiro passo: coleta todas as pastas + contagem direta
    resultado = []

    for dirpath, dirnames, filenames in os.walk(raiz_path):
        dirnames.sort()   # ordem alfabética
        p     = pathlib.Path(dirpath)
        nivel = len(p.relative_to(raiz_path).parts)
        info = {
            'caminho'    : p,
            'nome'       : p.name if nivel > 0 else raiz_path.name,
            'nivel'      : nivel,
            'arq_direto' : len(filenames),
            'arq_total'  : 0,   # será calculado a seguir
        }
        resultado.append(info)

    # Segundo passo: calcula o total recursivo (pasta + todas as subpastas)
    for info in resultado:
        caminho_pasta = info['caminho']
        total = 0
        for outro in resultado:
            try:
                outro['caminho'].relative_to(caminho_pasta)
                total += outro['arq_direto']
            except ValueError:
                pass
        info['arq_total'] = total

    return resultado


# ── 2. Gera arquivo TXT com árvore visual + total ─────────────
def gerar_txt(pastas: list[dict], saida: pathlib.Path, raiz_nome: str):
    linhas = []

    # Linha da raiz
    raiz_info = next((p for p in pastas if p['nivel'] == 0), None)
    if raiz_info:
        linhas.append(f"📁 {raiz_nome}  [{raiz_info['arq_total']}]\n")

    for p in pastas:
        if p['nivel'] == 0:
            continue
        indent = "│   " * (p['nivel'] - 1) + "├── "
        linhas.append(f"{indent}📁 {p['nome']}  [{p['arq_total']}]\n")

    with open(saida, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    print(f"  ✔ TXT gerado: {saida}")


# ── Main ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "═" * 50)
    print("   Mapeador de Hierarquia de Pastas (com contagem)")
    print("═" * 50)

    raiz_path = pathlib.Path(PASTA_RAIZ)
    print(f"\n  Lendo: {raiz_path}")

    pastas = coletar_pastas(PASTA_RAIZ)

    total_arquivos = sum(p['arq_direto'] for p in pastas)
    print(f"  Pastas encontradas  : {len(pastas)}")
    print(f"  Arquivos encontrados: {total_arquivos}\n")

    gerar_txt(pastas, SAIDA_TXT, raiz_path.name)

    print(f"\n  Pronto! Arquivo salvo em:\n  {SCRIPT_DIR}\n")