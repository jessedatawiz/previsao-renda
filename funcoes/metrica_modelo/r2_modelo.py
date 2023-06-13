import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


def r2_modelo(df_test, modelo):


    # Colunas utilizadas para a formula patsy 
    colunas_modelo = ['sexo_M', 'posse_de_imovel_True', 
                    'posse_de_veiculo_True', 
                    'idade', 'tempo_emprego', 'renda']

    X_test = df_test[colunas_modelo]

    # Variável resposta blablablabla
    y_test = X_test['renda']

    y_pred = modelo.predict(X_test)

    # Calculo do R² para a base de testes
    r2 = r2_score(y_test, y_pred)

    return r2

