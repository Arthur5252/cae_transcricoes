import requests
import logging
from datetime import datetime

def criar_json_resumo(data, resumo):

    linhas = resumo.split('. ')  # Divide com base no ponto seguido de espaço
    resumo_resumo = '. '.join(linhas[:2])  # Juntando as 3 primeiras sentenças
    data = datetime.now().strftime("%d/%m/%Y")
    print(type(data))
    #data_formatada = data.strftime("%d/%m/%Y")
    resultado = {
        "titulo": f'Reunião da Comissão de Assuntos Econômicos {str(data)}',
        "conteudo": resumo,
        "resumo": resumo_resumo,      
        "num_paginas": '',
        "UF": '',
        "Palavras-chave": '',
        "data": data, 
        "emissora": 'CAE - Comissão Assuntos Econômicos',
        "tema": 'CAE - Comissão Assuntos Econômicos',
        "tipoextracao": 'PDF'
    }

    payload = {
            "codigo": "",
            "titulo": resultado["titulo"],
            "conteudo": resultado['conteudo'],
            "orders": "",
            "prioridade": "",
            "exibicao": "S",
            "cdlink": "",
            "datainicio": '',
            "datafim": '',
            "ativo": "S",
            "criado": "",
            "atualizado": '',
            "usuariocriacao": '',
            "usuarioatualizacao": '',
            "urllink": "",
            "urllinkimg": "",
            "estadonoticia": "",
            "tipoextracao": resultado['tipoextracao'],
            "paginaextracao": "",
            "datanoticia": data,
            "tema": "",
            "emissora": "CAE",
            "urlbase": ""
        }

    print(payload)
    post_url = r'http://api.octopustax.com.br/informative/v1/news'

    try:
        post_response = requests.post(post_url, json=payload)
        post_response.raise_for_status()  # Levanta um erro se a resposta foi um erro HTTP
        logging.info(f"Resumo enviado com sucesso")
    except requests.exceptions.RequestException as e:
        logging.warning(f"Falha ao enviar resumo | Erro: {e}")


resumo = "## Relatório sobre a Reunião da Comissão de Assuntos Econômicos\n\n### Introdução\n\nNo dia 17 de dezembro de 2024, ocorreu a 7ª reunião da Comissão de Assuntos Econômicos (CAE) do Senado Federal, marcada pela discussão de diversas questões relevantes para a economia do Brasil, incluindo propostas de lei, análise de crédito externo e reflexões sobre a reforma tributária. Este resumo visa apresentar os principais tópicos discutidos na reunião, enfocando os impactos econômicos das decisões da comissão, as políticas públicas propostas e as visões dos senadores sobre o estado atual da economia nacional.\n\n### 1. Mensagens e Propostas de Crédito Externo\n\n#### Mensagem Nº 1558-2024\nA reunião começou com a apresentação da Mensagem nº 1558-2024 da Presidência da República, que encaminhou o relatório de avaliação das receitas e despesas primárias referente a novembro de 2024. Este documento, segundo a presidência da comissão, estará disponível para consulta pública por 15 dias, permitindo que os membros solicitassem autuação.\n\n#### Votos sobre Propostas de Crédito\nDiversas mensagens destinadas à autorização de operações de crédito externo foram discutidas ao longo da reunião, cujas principais características e finalidades foram apresentadas. Os senadores avaliaram e votaram favoravelmente a algumas destas medidas:\n\n- **Mensagem SF Nº 62/2024**: Autorização para contratação de operação de crédito de aproximadamente 57 milhões de dólares para o município de Serra, Espírito Santo, visando o programa de requalificação sustentável e mobilidade urbana.\n- **Mensagem SF Nº 77/2024**: Aprovação de empréstimo de 125 milhões de dólares para o programa de inclusão social e territorial de Salvador, Bahia.\n- **Mensagem SF Nº 79/2024**: Solicitação de 110 milhões de dólares para reestruturação de Sergipe, no âmbito do programa \"Sergipe mais próspero e sustentável\".\n- **Mensagem SF Nº 80/2024**: Autorização de 300 milhões de dólares ao novo programa Bolsa Família, visando o fortalecimento da assistência social para famílias em situação de vulnerabilidade.\n\nEsses empréstimos são fundamentais para o financiamento de projetos que buscam promover desenvolvimento sustentável e inclusão social nos respectivos estados.\n\n### 2. Comentários sobre a Reforma Tributária\n\nA reforma tributária continuou sendo uma fervorosa pauta de debate, com senadores expressando suas preocupações sobre as propostas em tramitação na Câmara dos Deputados, que alegadamente desconsideravam o trabalho já feito pelo Senado.\n\n#### Intervenções durante a reunião\n- **Senador Isauci** expressou a necessidade de maior tempo para discutir as emendas relacionadas à reforma e mencionou as possíveis consequências para o Benefício de Prestação Continuada (BPC) e para outros auxílio, chamando atenção para as \"maldades\" que poderiam ser implementadas sem uma análise detalhada.\n- Durante os debates, a relevância do Senado como casa revisora foi discutida, com apelos para que o Senado se posicione mais firmemente em perguntas legislativas que afetam diretamente a economia.\n- Foi destacado que a equipe da CAE trabalhou em grupos de trabalho para aprimorar a proposta de reforma tributária, e as sugestões foram incorporadas às emendas da PEC 22.\n\nA discussão da reforma tributária é crucial, pois tem potencial para impactar diretamente a estrutura fiscal do país e a distribuição de recursos entre Estados e Municípios. Além disso, a questão da transparência e justiça tributária foi central nos debates.\n\n### 3. Projetos de Lei Relevantes\n\n#### Projeto de Lei nº 1103/2022\nEntre as propostas revisadas, o Projeto de Lei nº 1103/2022, que visa estabelecer assistência material e abrir linhas de crédito para agricultores familiares, foi aprovado. Este projeto é significativo devido à sua ligação com a agricultura familiar, que representa uma parte vital da economia brasileira. A proposta inclui:\n\n- Abertura de linhas de crédito para recuperação de solos e pastagens.\n- Reconhecimento da importância da agricultura familiar na alimentação e na economia de pequenos municípios brasileiros.\n\nO parecer enfatizou que a agricultura familiar é responsável por uma grande parte da produção de alimentos no Brasil, contribuindo para 70% do feijão e 60% da produção de leite, por exemplo. Com a aprovação, busca-se assegurar a segurança jurídica e condições melhores para o trabalho rural, promovendo uma economia mais robusta no campo.\n\n### 4. Projetos e Políticas de Segurança Alimentar e Animal\n\nO Projeto de Lei nº 801/2024, que visa regulamentar a doação de alimentos e melhorar a segurança alimentar no país, foi discutido. Este projeto:\n\n- Tem como objetivo enfrentar a insegurança alimentar, que ainda afeta milhões de brasileiros.\n- Propõe incentivos para doações, reduzindo a carga tributária sobre doadores.\n\nOs senadores também debateram questões relacionadas à responsabilidade civil em casos de doações de alimentos, buscando garantir a segurança jurídica para aqueles que contribuem sem fins lucrativos.\n\n### 5. Reflexões Finais e Agradecimentos\n\nA reunião terminou com reflexões sobre o trabalho realizado ao longo dos últimos dois anos na CAE. O presidente da comissão, **Senador Vanderlain Cardoso**, fez um balanço das 127 reuniões realizadas e dos quase 300 projetos de lei aprovados, destacando a produtividade e a relevância das matérias debatidas. Também foram expressos agradecimentos aos colegas senadores, ao corpo técnico da comissão e à equipe de servidores.\n\nO senador agradeceu o apoio e a participação ativa de todos os membros, destacando a contribuição significativa da CAE para a construção de um Brasil melhor, mais justo e mais equitativo economicamente.\n\n## Conclusão\n\nA reunião da Comissão de Assuntos Econômicos do Senado evidenciou a seriedade e a dedicação dos senadores em tratar assuntos cruciais para a economia brasileira. As deliberações sobre crédito externo, a reforma tributária e os projetos voltados para a agricultura familiar e a segurança alimentar ilustram a importância do diálogo e da cooperação no desenvolvimento de políticas públicas eficazes. Este fluxo de trabalho e a grande produtividade da comissão são passos importantes para enfrentar os desafios econômicos do Brasil."
data = '24/01/01'
criar_json_resumo(data, resumo)