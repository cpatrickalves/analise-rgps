# Análise dos dados do Regime Geral de Previdênvia Social 

Este projeto visa realizar uma análise dos dados do Regime Geral de Previdência Social (RGPS) no período de 1995 a 2016.

As análises foram feitas por etapas utilizando as linguagens Python e SQL. Para cada etapa/análise foi criado um arquivo no Jupyter Notebook (extensão .ipynb), conforme descrito abaixo:

* [*analise-geral.ipynb*](https://github.com/cpatrickalves/analise-rgps/blob/master/analise-geral.ipynb) - apresenta uma visão geral da estrutura do banco de dados e dos dados contidos em cada tabela.
* *analise-aposentadorias.ipynb* - ...em desenvolvimento.

## Origem dos dados:

Em abril de 2017 foi instaurada a Comissão Parlamentar de Inquérito do Senado destinada a investigar a contabilidade da Previdência Social, esclarecendo com precisão as receitas e despesas do sistema, bem
como todos os desvios de recursos. Dentre todos os requerimentos criados durante a CPI, o requerimento N° 040/2017 solicitou ao Ministério da Fazenda informaçõe sobre os benefícios previdênciários (microdados)concedidos pelo RGPS no período compreendido entre 1995 e 2016. 

Em resposta ao requerimento, a Secretaria da Previdência do MF providenciou a extração dos dados solicitados pela Dataprev mantidos na base do Sistema Único de Beneficios - SUB.

As informações sobre o requerimento, resposta e dados originais estão disponíveis no item 97 (Arquivos DOC097 e Mídia 019) da página de documentos recebidos CPI da Previdência: http://legis.senado.leg.br/comissoes/docsRecCPI?codcol=2093

Os dados foram disponibilizados em formatos CSV, juntamente com o arquivo de dicionário das variáveis além de algumas tabelas no formato xlsx.

Para facilitar a manipulação dos dados, estes foram importados para um banco de dados SQLite3 utilizando o script **csv_to_sqlite3.py** disponível na pasta **util/** do projeto.

O banco de dados no formato SQLite3 está disponível para download neste [link](https://drive.google.com/drive/folders/1Mo6T6qU786GuOq-gMU322DmZzMCBlq3y?usp=sharing).

## Conteúdo dos dados

Os dados análisados possuem informações (microdados) sobre os registros de benefícios previdenciários para o período de 1995 a 2016.

Os benefícios contidos nos dados são:
* Aposentadoria por tempo de serviço de professor	
* Aposentadoria por tempo de serviço especial
* Aposentadoria por invalidez por acidente do trabalho
* Aposentadoria por invalidez previdenciária
* Auxílio-doença por acidente do trabalho
* Aposentadoria por tempo de serviço previdenciária
* Aposentadoria por idade
* Auxílio-doença previdenciário
* Pensão por morte por acidente do trabalho
* Pensão por morte previdenciária	

No total, a bases de dados somam mais de 65 milhões de registros.

O detalhamento das informações contidas em cada registro pode ser visto no arquivo *metadados.xls* disponível na pasta *microdados*.

## Reproduzindo as Análises

Para reproduzir os resultados será necessário instalar o Python (3.5 ou superior) e diversos os pacotes para manipulação de dados.

O recomendado é a instalação da distribuição Python Anaconda que já possui todos os pacotes Python necessários pré-instalados. O Anaconda pode ser obtido neste [link](https://anaconda.org/anaconda/python).

Após a instalação do Python e [download](https://github.com/cpatrickalves/analise-rgps/archive/master.zip) dos arquivos do projeto, a partir do Anaconda Navigator ou terminal/prompt basta a abrir a aplicação [Jupyter Notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) ou [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)(recomendado). 

Além dos arquivos do projeto, é necessário o [download do banco de dados](https://drive.google.com/drive/folders/1Mo6T6qU786GuOq-gMU322DmZzMCBlq3y?usp=sharing) no formato SQlite3. Após o download do banco, deve-se salvar os arquivos na seguinte estrutura de diretórios: *analise-rgps/microdados/sqlite3/microdadosRGPS.db*. Caso você deseje salvar o banco é um local diferente será necessário atualizar o caminho para o banco nos arquivos do jupyter notebook.

Por fim, dentro do Jupyter é possível carregar e executar os notebooks (arquivos com extensão **.ipynb**) do projeto.


