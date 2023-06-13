import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def matriz_correlacao(df, modelo: str):


    # Colunas utilizadas para o ajuste do modelo
    colunas = ['qtd_filhos', 'idade', 'tempo_emprego', 
               'renda', 
               'posse_de_veiculo_True', 'posse_de_imovel_True']
    
    # Calcula a matriz de spearman
    matriz_corr = df[colunas].corr(method='spearman')
    # Configurações do gráfico
    mask = np.triu(np.ones_like(matriz_corr, dtype=bool))

    sns.heatmap(matriz_corr, 
                annot=True, 
                cmap="Greens", 
                fmt=".2f",
                linewidths=0.5,
                mask=mask)

    # Configurações adicionais
    plt.title(f"Matriz de Correlação de Spearman - {modelo}")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(f"./output/matriz_correlacao_{modelo}.png")
    plt.show()

    return None