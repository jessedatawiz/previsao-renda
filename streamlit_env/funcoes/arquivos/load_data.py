import pandas as pd

def load_data(arquivo):


    try:
        df = pd.read_feather(arquivo)
        return df
    except FileNotFoundError:
        print(f"Arquivo não encontrado")
        return None
    except Exception as error:
        print(f"Erro: {error}")
        return None