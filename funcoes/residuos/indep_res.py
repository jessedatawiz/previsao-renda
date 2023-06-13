import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Verifica a independência do modelo através do cálculo de resíduos da varíavel 'log_renda'.
Possíveis outliers são identificados nesse plot.
'''
def indep_res(df: pd.DataFrame, modelo):

    if 'renda' in df.columns:
        try:
            df['log_renda'] = np.log(df['renda'])
        except Exception as erro:
            print(erro)
    
    sns.residplot(x=modelo.predict(), y='log_renda', data=df, lowess=True, 
                     scatter_kws={'alpha': 0.5}, 
                     line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});

    plt.xlabel('Valores Preditos')
    plt.ylabel('Resíduos')
    plt.title('Gráfico de Resíduos versus Valores Preditos')
    plt.savefig('./output/indepencia_res_log.png')
    plt.show()