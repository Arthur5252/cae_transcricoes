from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from datetime import datetime

def extrair_urls(url):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Ativar o modo headless
    chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU (opcional)
    chrome_options.add_argument("--no-sandbox")  # Prevenção de erros no Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # Melhor performance em containers
    url = 'https://legis.senado.leg.br/atividade/comissoes/comissao/38/'
    lista_urls = []
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    navegador.get(url)

    #data_atual = datetime.now().strftime('%d/%m/%Y')
    data_atual="17-12-2024"
    time.sleep(2)
    navegador.find_element(By.ID, 'btn_picker_mes_anterior').click()
    time.sleep(2)
    valida = navegador.find_elements(By.CLASS_NAME, 'painel-data-hora--data')[0].text
    print(valida)
    realizada=navegador.find_element(By.CLASS_NAME,'situacao-reuniao--realizada').get_attribute('title')
    print(realizada)
    if valida.replace('/','-')+'-2024' == data_atual and realizada == 'Realizada':
        print('entrou no if')
        time.sleep(2)
        navegador.find_element(By.CLASS_NAME,'painel-reuniao-corpo-texto').click()
        trechos = navegador.find_elements(By.CLASS_NAME, 'sf-js-player-reuniao--link-play')
        for i in trechos:
            lista_urls.append(i.get_attribute('href'))
        return lista_urls
    else:
        return 'Não é a edição mais atual'
