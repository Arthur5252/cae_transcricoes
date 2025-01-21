import os
import re
import whisper
from openai import OpenAI
import logging
import nltk
from helpers import *

def transcrever_audio_whisper(caminho_audio):
    """
    Transcreve um arquivo de áudio usando o modelo Whisper.
    """
    modelo = whisper.load_model('small')
    resultado = modelo.transcribe(caminho_audio)
    return resultado['text']

def extrair_numero(nome_arquivo):
    """
    Extrai o número do nome do arquivo.
    """
    match = re.search(r'(\d+)', nome_arquivo)
    return int(match.group(0)) if match else float('inf')

def resumir_texto(texto):
    prompt = f'Assuma o papel de um redator de relatórios especialista em economia.Enfatize as discussões sobre impactos econômicos e políticas públicas mencionadas na reunião.O resumo deve conter introdução, pontos principais discutidos e conclusões, se possível utilizando tópicos para melhorar a legibilidade.O texto a seguir é a transcrição de uma reunião da Comissão de Assuntos Econômicos, é uma reunião longa sobre assuntos tributários.Por favor faça um resumo de no minimo 1500 palavras desta transcrição: \n{texto}'
    cliente=OpenAI(api_key= "Sua chave api aqui")
    try:
        resposta = cliente.chat.completions.create(
            model="gpt-4o-mini",  # ou "gpt-4"
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000 # Defina o número máximo de tokens
        )
        return resposta.choices[0].message.content  # Retorna o resumo
    except Exception as e:
        print(f"Erro ao chamar a API do GPT: {e}")
        return texto  # Retorna o texto original em caso de erro

def transcrever_pasta(pasta_entrada, arquivo_saida):
    """
    Transcreve todos os arquivos .mp3 em uma pasta e salva as transcrições em um arquivo de texto.
    """
    print(pasta_entrada)
    print(arquivo_saida)
    nltk.download('punkt')
    transcricoes = []
    lista_arquivos = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.lower().endswith('.mp4')]
    lista_arquivos.sort(key=extrair_numero)

    for arquivo in lista_arquivos:
        caminho_mp3 = os.path.join(pasta_entrada, arquivo)
        print(f"Transcrevendo: {caminho_mp3}")

        try:
            texto = transcrever_audio_whisper(caminho_mp3)
            transcricoes.append(f"{texto}\n")
        except Exception as e:
            print(f"Erro ao transcrever {arquivo}: {e},  {caminho_mp3}")

    # Junta todas as transcrições em uma única string
    texto_completo = ''.join(transcricoes)

    # Resume o texto
    logging.info("-----------------------------Resumindo a Reunião-----------------------------")
    print("-----------------------------Resumindo a Reunião-----------------------------")
    resumo = resumir_texto(texto_completo)

    # Salva o resumo em um arquivo de texto
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(resumo)
    logging.info(f"-----------------------------Resumo das transcrições salvo em: {arquivo_saida}-----------------------------")
    print(f"-----------------------------Resumo das transcrições salvo em: {arquivo_saida}-----------------------------")
    return resumo
