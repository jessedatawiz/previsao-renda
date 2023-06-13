import pandas as pd
import  matplotlib.pyplot as plt

def plotar_grafico(tabela_perfil):


    """
    Plota um gráfico de dispersão da média do tempo de emprego pela média do log-renda.
    
    Args:
        tabela_perfil (pd.DataFrame): Tabela de perfil contendo os dados para plotagem.
    """
    
    # Plotando a média do tempo de emprego pela média do log-renda
    plt.figure(figsize=(10, 6))
    plt.scatter(tabela_perfil['Média do Log-Renda'], tabela_perfil['Média do Tempo de Emprego'])
    plt.xlabel('Média do Log-Renda')
    plt.ylabel('Média do Tempo de Emprego')
    plt.title('Média do Tempo de Emprego vs Média do Log-Renda')
    plt.savefig('./output/media_temporal_tempo_trabalho.png')
    plt.show()