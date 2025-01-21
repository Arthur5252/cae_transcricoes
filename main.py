import os
import logging
from processar_url import *
from baixar_arquivos import *
from converte_audio_em_texto import *
from criar_json import *
from extrai_data import *

# Configuração do logging
logging.basicConfig(level=logging.INFO, 
format='%(asctime)s - %(levelname)s - %(message)s', 
filename='transcricao_log.txt',  # Log será salvo neste arquivo
filemode='w')  # 'w' para sobrescrever

def main():
    inicio_exec = time.time()
    
    url = 'https://legis.senado.leg.br/atividade/comissoes/comissao/38/'
    caminho_pasta = r'C:\Users\Arthur\1_Projetos_Octopus\EAD\cae_transcricoes\arquivos_mp4'
    logging.info("---------------------------------------inicio da execução---------------------------------------")
    
    # Extrai URLs
    lista_urls = extrair_urls(url)
    logging.info(f'URLs extraídas: {lista_urls[1:]}')
    transcricoes = []
    if isinstance(lista_urls, list):
        for url in lista_urls:
            # Cria um caminho de arquivo único para cada vídeo
            caminho_arquivo = os.path.join(caminho_pasta, 'video.mp4')
            try:
                baixar_video(url, caminho_arquivo)
                logging.info(f'Vídeo baixado com sucesso: {caminho_arquivo}')
                transcri = transcrever_audio_whisper(caminho_arquivo)
                logging.info('Vídeo transcrito')
                transcricoes.append(transcri)
                os.remove(caminho_arquivo)
            except Exception as e:
                logging.error(f'Erro ao baixar vídeo de {url}: {e}')
        data= data_reuniao()
        arquivo_saida = fr'transcricao_{data}.txt'  # Nome do arquivo de saída
        texto_completo = ''.join(transcricoes)
        resumo = resumir_texto(texto_completo)
        
        criar_json_resumo(data,resumo)

        fim_exec=time.time()
        temp_exec = (fim_exec-inicio_exec)/60
        logging.info(f'O tempo de execução foi de {temp_exec:.2f}minutos!')
        logging.info("---------------------------------------Fim da execução---------------------------------------")
    else:
        print('O programa não será executado pois a reunião mais recente não é compativel com a data atual')

if __name__ == "__main__":
    main()