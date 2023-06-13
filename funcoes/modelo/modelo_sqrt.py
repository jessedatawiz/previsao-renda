import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


"""
sqrt: raiz quadrada
df: apenas com variáveis dummies
A formula inclui todas as variáveis
"""
def modelo_sqrt(df_train: pd.DataFrame):


    formula = ('renda ~ '
           ' + sexo_M + '
           'posse_de_imovel_True + qtd_filhos + '
           'posse_de_veiculo_True + '
           'idade + '
           'I(np.sqrt(tempo_emprego))')
    
    # inicia o patsy dmatrices
    y_train, X_train = patsy.dmatrices(formula, data=df_train)

    model_ols = sm.OLS(y_train, X_train)
    fitted_model = model_ols.fit()
    
    return fitted_model
