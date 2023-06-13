"""
Salva métricas em .txt
"""

def save_file(metrica, filename):
    try:
        with open(filename, 'w') as file:
            file.write(str(metrica))
    except Exception as error:
        print(f"Erro: {error}")