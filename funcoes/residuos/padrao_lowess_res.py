import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def residuos_lowess(df: pd.DataFrame, modelo):
    """
    Plota uma grade de gráficos de dispersão dos resíduos em relação a diferentes variáveis,
    juntamente com as curvas LOWESS suavizadas.
    """

    # Cálculo dos resíduos do modelo
    residuos = modelo.resid

    try:
        fig, axs = plt.subplots(3, 2, figsize=(12, 12))
        # Features utilizadas para o modelo inicial
        variaveis = [df[coluna] for coluna in ['tempo_emprego', 'posse_de_imovel_True', 
                                            'qtd_filhos', 'posse_de_veiculo_True', 
                                            'idade']]

        titulos = ['Tempo Emprego', 
                'Posse de Imóvel', 
                'Quantidade de Filhos', 
                'Posse de Veículo', 
                'Idade']

        for i in range(3):
            for j in range(2):
                axs[i, j].scatter(variaveis[i*2+j], residuos)
                axs[i, j].set_xlabel(titulos[i*2+j])
                axs[i, j].set_ylabel('Resíduos')
                axs[i, j].set_title(f'Resíduos vs {titulos[i*2+j]}')

                lowess_fit = sm.nonparametric.lowess(residuos, variaveis[i*2+j])
                axs[i, j].plot(lowess_fit[:, 0], lowess_fit[:, 1], color='red')

        plt.tight_layout()
        plt.savefig(f'./output/padrao_residuos_{modelo}.png')
        plt.show()

        return residuos
    
    except Exception as erro:
        mensagem = f'Ocorreu um erro: {erro}'
        return mensagem