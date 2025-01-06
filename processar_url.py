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

    data_atual = datetime.now().strftime('%d/%m/%Y')
    time.sleep(2)
    navegador.find_elements(By.CLASS_NAME, 'situacao-reuniao--realizada')[0].click()
    time.sleep(1)
    valida = navegador.find_elements(By.CLASS_NAME, 'px-2')[0].text
    if valida.replace(' às 10h', '') == data_atual:
        time.sleep(2)
        trechos = navegador.find_elements(By.CLASS_NAME, 'sf-atv-cmss-item-video')
        for i in trechos:
            lista_urls.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        return lista_urls
    else:
        return 'Não é a edição mais atual'