# Infnet - Projeto final

## Análise de Tópicos relacionados ao Operador Nacional do Sistema Elétrico

<b>Objetivo:</b> Identificar tópicos de relevância para o Operador Nacional do Sistema Elétrico.

### Fases:

* Data Collection: Aquisição de dados através da API do Twitter. Foram coletados tweets utilizando os seguintes termos de busca:
  * Operador Nacional do Sistema Elétrico
  * eletricidade & infraestrutura
  * energia & infraestrutura
  * infraestrutura elétrica
  * "geração de energia"
  * "sistema elétrico"
  * "energia elétrica"
  * ONS
 
* Data Wrangling: Os dados coletados foram manipulados para que estivessem no formato apropriado para sua utilização no modelo. Portanto, foram removidos emojis, símbolos, mentions, urls, hashtags. Foram removidas as stopwords e também os termos de busca relacionado ao tweet, de forma a diminuir o viés trazido com eles. Os tweets limpos foram, por fim, transformados em tokens.

* Modelling: Para identificar os tópicos foi utilizado o algoritmo GSDMM, por ter melhor resultado em textos curtos (como tweets). Os parametros escolhidos foram: K: 50, alpha: 0.1, beta: 0.1, número de iterações: 15.

* Análise dos resultados: Foram selecinados os 15 tópicos com mais documentos e foi realizada a visualização das palavras pertencentes a cada grupo através de Nuvem de Palavras.

### Estrutura:

Este projeto se divide em três diretórios:
* Code: contém script em python e Jupyter notebooks correspondentes das fases de coleta, manipulação e modelagem.
* Data: contém os arquivos csv dos dados coletados na API do Twitter (raw) e os arquivos csv e json dos dados após a fase de preprocessamento.
* Docs: contém a apresentacão em ppt do projeto.
