import os
import logging
from processar_url import *
from baixar_arquivos import *
from converte_audio_em_texto import *
from limpa_pasta import *
from datetime import datetime

# Configuração do logging
logging.basicConfig(level=logging.INFO, 
format='%(asctime)s - %(levelname)s - %(message)s', 
filename='transcricao_log.txt',  # Log será salvo neste arquivo
filemode='w')  # 'w' para sobrescrever, 'a' para anexar

def main():
    inicio_exec = time.time()
    
    url = 'https://legis.senado.leg.br/atividade/comissoes/comissao/38/'
    caminho_pasta = 'C:\\Users\\Usuário\\Documents\\1_Projetos_Octopus\\cea_transcricoes\\arquivos_mp4'
    logging.info("---------------------------------------inicio da execução---------------------------------------")
    
    # Extrai URLs
    lista_urls = extrair_urls(url)
    print(lista_urls)
    logging.info(f'URLs extraídas: {lista_urls[1:]}')
    if isinstance(lista_urls, list):
        for index, url in enumerate(lista_urls[1:], start=1):
            # Cria um caminho de arquivo único para cada vídeo
            caminho_arquivo = os.path.join(caminho_pasta, f'video_{index}.mp4')
            try:
                baixar_video(url, caminho_arquivo)
                logging.info(f'Vídeo {index} baixado com sucesso: {caminho_arquivo}')
            except Exception as e:
                logging.error(f'Erro ao baixar vídeo {index} de {url}: {e}')

        data_atual = datetime.now().strftime('%d-%m-%Y')  # Formata a data atual
        arquivo_saida = fr'transcricao_{data_atual}.txt'  # Nome do arquivo de saída

        try:
            transcrever_pasta(pasta_entrada=caminho_pasta, arquivo_saida=arquivo_saida)
            logging.info(f'------------------Transcrição concluída e salva em: {arquivo_saida}------------------')
        except Exception as e:
            logging.error(f'Erro ao transcrever arquivos de áudio: {e}')
        
        limpa_pasta(pasta=caminho_pasta)
        fim_exec=time.time()
        temp_exec = (fim_exec-inicio_exec)/60
        logging.info(f'O tempo de execução foi de {temp_exec:.2f}minutos!')
        logging.info("---------------------------------------Fim da execução---------------------------------------")
    else:
        print('O programa não será executado pois a reunião mais recente não é compativel com a data atual')

if __name__ == "__main__":
    main()