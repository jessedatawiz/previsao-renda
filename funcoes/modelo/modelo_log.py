import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


"""
lr: linear regression
df: apenas com variáveis dummies
A formula inclui todas as variáveis
"""
def modelo_log(df: pd.DataFrame):


    formula = ('np.log(renda) ~ '
           ' + sexo_M + '
           'posse_de_imovel_True + '
           'posse_de_veiculo_True + '
           'idade + '
           'tempo_emprego -1')
    
    # inicia o patsy dmatrices
    y, X = patsy.dmatrices(formula, data=df)

    model_ols = sm.OLS(y, X)
    fitted_model = model_ols.fit()
    
    return fitted_model
