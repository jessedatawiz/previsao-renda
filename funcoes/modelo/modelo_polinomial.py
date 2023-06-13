import sys
sys.path.insert(0, './funcoes/')

import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


"""
pol: polinomial
df: apenas com variáveis dummies
A formula inclui todas as variáveis
"""
def modelo_pol(df: pd.DataFrame):


    formula = ('renda ~ '
           ' + sexo_M + '
           'posse_de_imovel_True + qtd_filhos + '
           'posse_de_veiculo_True + '
           'idade + '
           'I(tempo_emprego) + I(tempo_emprego**2) + I(tempo_emprego**3)')
    
    # inicia o patsy dmatrices
    y, X = patsy.dmatrices(formula, data=df)

    model_ols = sm.OLS(y, X)
    fitted_model = model_ols.fit()
    
    return fitted_model