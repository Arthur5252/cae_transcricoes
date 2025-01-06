import os

def limpa_pasta(pasta):# Caminho da pasta que você quer limpar
    # Loop para apagar cada arquivo dentro da pasta
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):  # Confirma se é um arquivo
            os.remove(caminho_arquivo)  # Apaga o arquivo
