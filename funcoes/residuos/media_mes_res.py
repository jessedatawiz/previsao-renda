import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def residuos_por_mes(df_original: pd.DataFrame, df_dummie: pd.DataFrame, residuos, modelo_tipo:str):
    """
    Avalia se o valor médio dos resíduos aparenta ter relação com o mês de referência.

    """
    try:
        # Adiciona a coluna 'data_ref' ao df dummie

        if 'data_ref' in df_original.columns:
            df_dummie['data_ref'] = df_original['data_ref']

        df_dummie['Residuos'] = residuos
        sns.boxplot(data=df_dummie, x=df_dummie['data_ref'].dt.month, y='Residuos',
                    notch=True, showcaps=False,
    flierprops={"marker": "x"},)
        plt.xlabel('Mês de Referência')
        plt.ylabel('Resíduos')
        plt.title('Relação entre Resíduos e Mês')
        plt.savefig(f'./output/residious_mes_{modelo_tipo}.png')
        plt.show()

    except Exception as e:
        msg = f"Ocorreu um erro ao plotar o gráfico: {str(e)}"
        return msg
