import matplotlib.pyplot as plt
import statsmodels.api as sm

def plot_influencia(modelo):

    """
    Os studentized residuals (resíduos studentizados) são uma medida dos resíduos
    padronizados de um modelo estatístico. Eles são calculados dividindo o resíduo 
    de cada observação pela estimativa do desvio padrão residual. Isso permite que
    você avalie o quão discrepante ou incomum é um determinado ponto em relação ao 
    padrão esperado.
    """

    # Método para calcular os outliers
    influencia = modelo.get_influence()

    # Retorna os 
    studentized_residuos = influencia.resid_studentized
    # Crie um gráfico de dispersão dos studentized residuals em relação aos valores previstos
    plt.scatter(modelo.predict(), studentized_residuos)
    plt.xlabel('Valores previstos')
    plt.ylabel('Studentized Residuals')
    plt.title('Gráfico de dispersão dos Studentized Residuals')
    plt.axhline(y=0, color='r', linestyle='--')  # Linha horizontal em y=0 para referência
    plt.savefig(f"./output/influencia_plot_{str(modelo)}.png")
    plt.show()

    return studentized_residuos