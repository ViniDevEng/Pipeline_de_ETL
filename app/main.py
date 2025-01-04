from selenium import webdriver
import pandas as pd
import time
import os

local_downloard_arquivo = r'D:\ÁREA DE TRABALHO\Pipeline_de_ETL\data\\'
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": local_downloard_arquivo,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

browser = webdriver.Chrome(options=options)
url = 'https://servicos.dpf.gov.br/dadosabertos/PALAS/'
browser.get(url)

time.sleep(5)
browser.find_element('xpath', '/html/body/pre/a[42]').click()
time.sleep(5)

tb = pd.read_csv(r'D:\ÁREA DE TRABALHO\Pipeline_de_ETL\data\PALAS_OPERACOES_2024_01.csv', encoding="latin-1", delimiter=";")
df = pd.DataFrame(tb)

print(df)