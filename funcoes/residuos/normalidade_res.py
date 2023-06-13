import matplotlib.pyplot as plt
import seaborn as sns

"""
Retorna a distribuição dos resíduos para um dado modelo.
"""
def normal_res(residuos, modelo: str):
    
    
    sns.displot(residuos, height=3, aspect=2);
    plt.ylabel("Contagem")
    plt.xlabel("Resíduos")
    plt.savefig(f"./output/dist_normal_res_{modelo}")
    plt.show()
    plt.tight_layout()

    return None