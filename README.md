# Projeto de Previsão de Renda usando Regressão Linear

Este projeto tem como objetivo desenvolver um modelo de regressão linear para prever a renda com base em um conjunto de variáveis preditoras. O modelo é construído utilizando a biblioteca Statsmodels em Python.

## Funcionalidades
* Pré-processamento dos dados
* Análise exploratória de dados
* Ajuste do modelo de regressão linear: implementa a regressão linear utilizando o método OLS (Ordinary Least Squares).
* Avaliação do modelo: analisa a significância estatística dos coeficientes, o R² e os resíduos para verificar a qualidade do ajuste.
* Identificação de outliers: identifica e remove outliers com base nos studentized residuals.
* Implementação no Streamlit: permite executar o projeto em uma interface interativa usando o Streamlit.

## Como usar
* Instale as dependências do projeto executando pip install -r requirements.txt.
* Execute o arquivo [pr_tratamento.py](./pr_tratamento_dados.ipynb) para realizar o pré-processamento dos dados e análise exploratória.
* Consulte o diretório [modelo](./funcoes/modelo) para ajustar o modelo de regressão linear.
* Consulte o diretório [metrica_modelo](./funcoes/metrica_modelo/) para avaliar o modelo e obter métricas de desempenho.
* Consulte o diretório [outliers](./funcoes/outliers/) para identificar e remover outliers.
* Os arquivos/gráficos resultantes estão salvos em [output](./output)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request para adicionar novas funcionalidades, corrigir bugs ou aprimorar o projeto.

## Autor
Jessé Rodrigues
