from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os

#functions__

def verifica_preco():
    if preco_antigo != preco_atual:
        print('Houve uma alterção no preço!')
    else:
        print('O preço continua o mesmo.')

#variables__
palavra_chave = 'const'
contador = 0
valores = []
linhas_texto = ''
padrao = r'\d+'
data_hora = datetime.datetime.now()
nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"

#app_action___
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = "https://www.leroymerlin.com.br/kit-200-abracadeiras-nylon-3,6x150mm-preto-pacote-kala_1567337335"
req = requests.get(url,headers=headers)
html_content = req.text
soup = BeautifulSoup(html_content, "html.parser")

#data_get___
prod_barcode = soup.find('div', class_ = 'badge product-code badge-product-code').text

prod_title = soup.find('h1', class_ = 'product-title align-left color-text').text

prod_price = soup.find('div', class_= 'product-price-tag')

#Write_archive__
with open(nome_arquivo, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(prod_price)

#Read_archive__
with open(nome_arquivo, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        linhas_texto = linhas_texto + '.'.join(row) + '\n'

#remove_archive__
os.remove(nome_arquivo)

#find_price__
for linha in linhas_texto.split('\n'):
    if palavra_chave in linha:
        match = re.search(padrao, linha)
        if match:
            preco = match.group()
            valores.append(preco)
            contador += 1
            if contador >=2:
                break

#print_price__


preco_atual =float(','.join(valores).replace(",", "."))
preco_antigo =str(','.join(valores).replace(",", "."))

with open(nome_arquivo, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(preco_antigo)

with open(nome_arquivo, 'r') as file:
    preco_salvo = file.read().strip()
  

product = {'LM': [prod_barcode],
        'Title': [prod_title],
        'Price': [preco_atual]}

print(prod_barcode) 
print(prod_title)
print(preco_atual)
verifica_preco()
print(preco_salvo)
