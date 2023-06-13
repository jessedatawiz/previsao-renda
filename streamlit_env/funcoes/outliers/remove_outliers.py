import numpy as np
import pandas as pd
import statsmodels.api as sm


def remove_outliers(df, modelo, limite=1.8):


    # Método para calcular os outliers
    influencia = modelo.get_influence()

    # Retorna os studentized residuals
    studentized_residuos = influencia.resid_studentized

    # Identifique os índices dos outliers
    indices_outliers = np.where((studentized_residuos > limite) | (studentized_residuos < -limite))[0]

    # Remova os outliers do DataFrame
    df_sem_outliers = df.drop(indices_outliers)

    removidos_outliers = df.shape[0] - df_sem_outliers.shape[0]
    print(f"Número de outliers: {removidos_outliers}")

    return df_sem_outliers
