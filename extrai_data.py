from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def data_reuniao():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ativar o modo headless
    chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU (opcional)
    chrome_options.add_argument("--no-sandbox")  # Prevenção de erros no Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # Melhor performance em containers
    url = 'https://legis.senado.leg.br/atividade/comissoes/comissao/38/'
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    navegador.get(url)
    time.sleep(2)
    navegador.find_element(By.ID, 'btn_picker_mes_anterior').click()
    time.sleep(2)
    data=navegador.find_element(By.CLASS_NAME, 'painel-data-hora--data')
    data_reuniao = data.text
    print(data_reuniao)
    time.sleep(1)
    return data_reuniao.replace('/','-')
