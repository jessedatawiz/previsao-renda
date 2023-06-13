# importanto as bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import statsmodels.api as sm
import statsmodels.formula.api as smf

from load_data import load_data
from get_dummies import dummies_frequencia
from atividade_34_regressao_iii.blablabl_modelo import modelo_ols

# configura a pagina do navegador
st.set_page_config(page_title='Análise de Crédito - Ebanker', page_icon="💰")
st.title('Análise de Crédito')

# Carregamento do banco de dados

try:
    with st.spinner('Carregando base de dados'):   
        X_train, y_train, X_test, y_test = load_data(X_train='X_train.csv', 
                                             y_train='y_train.csv', 
                                             X_test='X_test.csv', 
                                             y_test='y_test.csv')
        
        # remonta o dataframe completo, tratado e original
        data = np.concatenate((X_train, y_train), axis=1)

except:
    st.error('Dados carregados incorretamente. Verficar.')

# Filtros 
tipo_renda_filter = st.sidebar.multiselect("Tipo de Renda", 
                                           data["tipo_renda"].unique(),
                                           default=data.tipo_renda.unique())

educacao_filter = st.sidebar.multiselect("Escolaridade", 
                                         data["educacao"].unique(),
                                         default=data.educacao.unique())

tipo_residencia_filter = st.sidebar.multiselect("Residência",
                                                data["tipo_residencia"].unique(),
                                                default=data["tipo_residencia"].unique())
idade_filter = st.sidebar.slider("Faixa Etária", 
                                 int(data["idade"].min()), 
                                 int(data["idade"].max()),
                                 (int(data["idade"].min()), int(data["idade"].max())))

estado_civil_filter = st.sidebar.multiselect("Estado Civil",
                                             data["estado_civil"].unique(),
                                             default=data["estado_civil"].unique())

# Aplicando os filtros
@st.cache_data()
def data_filter():
    data_filter = data[
        (data["tipo_renda"].isin(tipo_renda_filter)) &
        (data["educacao"].isin(educacao_filter)) &
        (data["tipo_residencia"].isin(tipo_residencia_filter)) &
        (data["idade"].between(idade_filter[0], idade_filter[1])) &
        (data["estado_civil"].isin(estado_civil_filter))
    ]
    return data_filter


# Os dados só aparecem após apertar botão de confirmação.
# Por isso o resto do código está condicionado ao botão.
# Ajeitar para rodar uma vez total.

if st.sidebar.button("Confirmar", use_container_width=True):
    data_filter = data_filter()
    
    # informacoes medias do bando de dados filtrado
    num_clientes = data_filter.shape[0]
    media_idade = data_filter.idade.mean().round(1)
    media_veiculo = data_filter.posse_de_veiculo.mean().round(2)
    media_imovel = data_filter.posse_de_imovel.mean().round(2)
    media_renda = data_filter.renda.mean().round(2)

    # secão dos clientes
    st.subheader("Ebankeners:")

    # definição das coluna # de clientes
    st.metric("Clientes", num_clientes, help="Número Total de Clientes")
    
    # definição das outras métricas
    (media_idade_col, 
    media_renda_col, 
    media_imovel_col, 
    media_veiculo_col) = st.columns(4)

    # lembrando que imovel e veiculos são bool, logo aparecerá a media de Trues
    with media_renda_col:
        st.metric("Renda (R$)", media_renda, help="Renda média")
    with media_idade_col:
        st.metric("Idade Média", media_idade)
    with media_veiculo_col:
        st.metric("Veículo (%)", media_veiculo, help="Posse de veículo")
    with media_imovel_col:
        st.metric("Imóvel (%)", media_imovel, help="Posse de imóvel")

    # colunas para os graficos
    col1, col2 = st.columns(2)

    fig_hist = px.histogram(data_filter, x="idade", nbins=10,
                       title='Idade',
                       opacity=0.8,
                       color=data_filter.sexo)
    fig_hist.update_layout(height=400, width=350)
    col1.plotly_chart(fig_hist)

   
    fig_pie = px.pie(data_filter, names="tipo_renda",
                    title="Tipo de Renda")
    fig_pie.update_layout(height=400, width=400)
    col2.plotly_chart(fig_pie)

    # titulo da seção Bens (imoveis e veiculos)
    st.subheader("Bens")
    
    # cria tabs para as categorias
    possui_imovel, possui_veiculo = st.tabs(["Imóvel", "Veículo"])
    
    with possui_imovel:
        col1_imovel, col2_imovel = st.columns(2)

        """
        Pelos dados previamente observados, mais de 6 pessoas por resisdência são poucas
        e não aparecem nos gráficos.
        """
        fig_hist_imovel = px.histogram(data_filter, x="qt_pessoas_residencia",
                       title='Pessoas por residência',
                       opacity=0.8,
                       color="posse_de_imovel",
                       range_x=(0,6))
        fig_hist_imovel.update_layout(height=400, width=350)
        col1_imovel.plotly_chart(fig_hist_imovel)

        fig_pie_imovel = px.pie(data_filter, names="tipo_residencia",
                    title="Tipo de Renda")
        fig_pie_imovel.update_layout(height=400, width=400)
        col2_imovel.plotly_chart(fig_pie_imovel)

    with possui_veiculo:
        st.header("Teste Veiculo")

#Inicio do modelo de regressao linear.

st.subheader("Regressão Linear")

# Baseado em análises prévias, será apenas analisado as variáveis explicitados na formula definida a seguir. 
# Ver atividade do módulo 13 para maiores informações.
# O modelo OLS (patsy) só pode ser iniciado após a criação de variáveis dummies.

# retornando as variáveis dummies
colunas=['tipo_renda', 
        'educacao', 
        'estado_civil', 
        'tipo_residencia',
        'posse_de_veiculo', 
        'posse_de_imovel']
                            

formula = ('np.log(renda) ~'
        '+ posse_de_imovel_True + qtd_filhos'
        '+ posse_de_veiculo_True'
        '+ qt_pessoas_residencia + idade'
        '+ tempo_emprego -1')

modelo = modelo_ols(formula, X_train, y_train, X_test, y_test, 'output_file.txt'):
st.write("Primeiro modelo")
st.write(f"R² ajustado: {modelo.rsquared_adj :.2f}")




