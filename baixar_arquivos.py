import requests

def baixar_video(url, caminho_arquivo):
    try:
        # Envia uma requisição GET para a URL do vídeo
        response = requests.get(url, stream=True)  # O parâmetro stream=True permite baixar o arquivo em partes
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida (status 200)

        # Abre um arquivo no modo de escrita binária
        with open(caminho_arquivo, 'wb') as arquivo:
            # Escreve o conteúdo do vídeo no arquivo
            for parte in response.iter_content(chunk_size=8192):  # Lê o conteúdo em partes
                arquivo.write(parte)

        print(f'Arquivo salvo em: {caminho_arquivo}')
        
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao baixar o vídeo: {e}')

