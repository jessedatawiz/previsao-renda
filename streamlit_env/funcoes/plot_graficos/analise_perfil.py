import pandas as pd
import numpy as np
def criar_tabela_perfil(df):


    """
    Cria uma tabela de perfil com base na categorização do tempo de emprego em quantis.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem analisados.
    
    Returns:
        pd.DataFrame: Tabela de perfil com a quantidade de observações, média do log-renda
                      e média do tempo de emprego para cada categoria.
    """
    # Categorize 'tempo_emprego' em 20 quantis
    df['tempo_emprego_categoria'] = pd.qcut(df['tempo_emprego'], q=20, duplicates='drop')

    # Criação da coluna log(renda)
    df['log_renda'] = np.log(df['renda'])

    # Criação da tabela de perfil
    tabela_perfil = pd.DataFrame()
    tabela_perfil['Observações'] = df.groupby('tempo_emprego_categoria').size()
    tabela_perfil['Média do Log-Renda'] = df.groupby('tempo_emprego_categoria')['log_renda'].mean()
    tabela_perfil['Média do Tempo de Emprego'] = df.groupby('tempo_emprego_categoria')['tempo_emprego'].mean()

    return tabela_perfil