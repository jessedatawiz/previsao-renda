import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

def calculate_vif(df):


    # Seleciona apenas as variáveis numéricas
    df_numeric = df.select_dtypes(include=np.number)
    
    # Excluindo a coluna qt_pessoas_residencia, que não foi usada na analise do modelo
    df.drop('qt_pessoas_residencia', axis=1)

    # Calcula o fator de VIF para cada variável
    vif_factors = [vif(df_numeric.values, i) for i in range(df_numeric.shape[1])]

    # Cria o DataFrame com os resultados
    vars_vif = pd.DataFrame({'Feature': df_numeric.columns, 'VIF Factor': vif_factors})
    vars_vif = vars_vif.round(2)

    return vars_vif
