import json
import requests
import logging

def criar_json_resumo(resumo):
    arquivo_saida = 'json_resumo.json'
    linhas = resumo.split('. ')  # Divide com base no ponto seguido de espaço
    resumo_resumo = '. '.join(linhas[:2])  # Juntando as 3 primeiras sentenças
    data_atual = ''
    resultado = {
        "titulo": f'Resumo da reunião da Comissão de Assuntos Econômicos.',
        "conteudo": resumo,
        "resumo": resumo_resumo,      
        "num_paginas": '',
        "UF": '',
        "Palavras-chave": '',
        "data": data_atual, 
        "emissora": 'CAE - Comissão Assuntos Econômicos',
        "tema": 'CAE - Comissão Assuntos Econômicos',
        "tipo_extracao": 'não sei ainda'
    }
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_json:
            json.dump(resultado, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Resultados resumidos exportados para {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao salvar o JSON: {e}")         

        payload = {
        "titulo": resultado["titulo"],
        "conteudo": resultado["conteudo"],
        "resumo": resultado["resumo"], 
        "urllink": '',
        "exibicao": "S",
        "ativo": "S",
        "urlbase": '',
        "emissora": resultado['emissora'],
        "tipoextracao": resultado['tipo_extracao'],#        "urllinkimg": "",
        "estadonoticia": resultado["UF"],
        "datanoticia": data_atual
    }

    print(payload)
    post_url = r'http://api.octopustax.com.br/informative/v1/news'

    try:
        #post_response = requests.post(post_url, json=payload)
        #post_response.raise_for_status()  # Levanta um erro se a resposta foi um erro HTTP
        logging.info(f"Resumo enviado com sucesso")
    except requests.exceptions.RequestException as e:
        logging.warning(f"Falha ao enviar resumo | Erro: {e}")
                                                                                                                                                                                                                                                                                                                                                             