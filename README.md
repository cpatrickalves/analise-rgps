# Análise dos dados do Regime Geral de Previdênvia Social 

Este projeto visa realizar uma análise descritiva completa dos dados do Regime Geral de Previdência Social (RGPS) no período de 1995 a 2016.

A análise foi feita por etapas utilizando a linguagem Python. Para cada etapa foi criado um arquivo no Jupyter Notebook (extensão .ipynb).

* *analise-geral.ipynb* - apresenta uma visão geral da estrutura do banco de dados e dos dados contidos em cada tabela.

## Origem dos dados:

Em abril de 2017 foi instaurada a Comissão Parlamentar de Inquérito do Senado destinada a investigar a contabilidade da Previdência Social, esclarecendo com precisão as receitas e despesas do sistema, bem
como todos os desvios de recursos. Dentre todos os requerimentos criados durante a CPI, o requerimento N° 040/2017 solicitou ao Ministério da Fazenda informaçõe sobre os benefícios previdênciários (microdados)concedidos pelo RGPS no período compreendido entre 1995 e 2016. 

Em resposta ao requerimento, a Secretaria da Previdência do MF providenciou a extração dos dados solicitados pela Dataprev mantidos na base do Sistema Único de Beneficios - SUB.

As informações sobre o requerimento, resposta e dados originais estão disponíveis no item 97 (Arquivos DOC097 e Mídia 019) da página de documentos recebidos CPI da Previdência: http://legis.senado.leg.br/comissoes/docsRecCPI?codcol=2093

Os dados foram disponibilizados em formatos CSV, juntamente com o arquivo de dicionário das variáveis além de algumas tabelas no formato xlsx.

Para facilitar a manipulação dos dados, estes foram importados para um banco de dados SQLite3 utilizando o script **csv_to_sqlite3.py** disponível na pasta **util/** do projeto.

O banco de dados está disponível para download neste [link](https://drive.google.com/drive/folders/1Mo6T6qU786GuOq-gMU322DmZzMCBlq3y?usp=sharing).


