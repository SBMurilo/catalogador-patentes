# Catalogador de Patentes

Ferramenta em Python para **catalogar, renomear e classificar patentes em PDF** a partir de dados coletados automaticamente (web scraping). Desenvolvida para organizar um acervo grande de patentes de engenharia, substituindo um trabalho manual repetitivo.

## O que faz

- **Coleta de dados:** busca cada patente no [Google Patents](https://patents.google.com) e extrai título, resumo, inventores, titular, datas e país. Para patentes brasileiras (PI, MU, C1...) usa o site do [INPI](https://busca.inpi.gov.br).
- **Download e renomeação:** baixa o PDF quando disponível e renomeia no padrão `Código_Titular_Título.pdf`.
- **Planilhas Excel:** registra tudo em uma planilha principal e envia os casos problemáticos (não encontrado, sem download, erro) para uma planilha de revisão.
- **Retomada segura:** ignora patentes já catalogadas, reinicia o navegador automaticamente quando ele trava e mantém uma fila de pendentes do INPI.
- **Classificação por palavras-chave:** a pasta `ferramentas/` classifica cada patente em uma hierarquia de pastas (até 3 níveis) com pontuação ponderada por especificidade dos termos.

## Estrutura

```
catalogador/          programa principal (menu no terminal)
  main.py             menu e fluxo de processamento
  scraper.py          Selenium + Google Patents
  inpi_scraper.py     Selenium + INPI (Brasil)
  normalizer.py       extração do código a partir do nome do PDF
  organizer.py        renomeia e move os PDFs finais
  excel_manager.py    leitura e escrita das planilhas
  utils.py            formatação de nomes, inventores e variações de código
  config.py           caminhos e lista de patentes de teste
ferramentas/          utilitários auxiliares
  organizar_patentes.py                 classifica e copia os PDFs para as pastas
  Patentes_Classificacao_Teorica.py     gera planilha de auditoria da classificação
  palavras_chave.py                     dicionário com ~12 mil termos em 358 pastas/subpastas
  mapear_pastas*.py                     mapeiam a árvore de pastas (com contagem de arquivos)
```

## Como usar

Requer Python 3.10+ e Google Chrome instalado.

```bash
pip install -r requirements.txt
```

1. Edite os caminhos em `catalogador/config.py` (planilhas e pastas de trabalho). Os valores atuais são exemplos de Windows.
2. Rode o menu:

```bash
cd catalogador
python main.py
```

| Opção | Ação |
|-------|------|
| 1 | Adicionar uma patente digitando o código |
| 2 | Processar a lista de teste de `config.py` |
| 3 | Catalogar os PDFs da pasta `Inserir` |
| 4 | Verificar consistência entre planilha e pasta de PDFs |
| 5 | Catalogar patentes do INPI (pode exigir resolver CAPTCHA) |

Classificação e auditoria (ajuste os caminhos no topo de cada script):

```bash
cd ferramentas
python organizar_patentes.py
python Patentes_Classificacao_Teorica.py --excel planilha.xlsx
```

## Tecnologias

Python, Selenium, pandas, openpyxl, BeautifulSoup, requests.

## Observações

- Os scrapers dependem do layout dos sites, que pode mudar.
- Os caminhos em `config.py` e nos scripts de `ferramentas/` são locais e precisam ser adaptados.
- Planilhas e PDFs não são versionados (ver `.gitignore`).
