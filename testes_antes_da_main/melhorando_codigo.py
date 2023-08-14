from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os
from openpyxl import load_workbook

#functions__
def verifica_preco(preco_salvo, preco_atual):
    if preco_salvo != preco_atual:
        print('Houve uma alterção no preço!')
    else:
        print('O preço continua o mesmo.')

#variables__
palavra_chave = 'const'
contador = 0
valor_real = []
valor_centavo = []
linhas_texto = ''
ean_13 = ''
padrao_real = r'\d+\.\d{3}|\d.\d{2}'
padrao_centavo = r'.\d{2}'
data_hora = datetime.datetime.now()
nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"

#app_action___
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = "https://www.leroymerlin.com.br/ar-condicionado-split-24000-btus-quente-e-frio-220v-series-a1-tcl_91697550?term=91697550&searchTerm=91697550&searchType=LM"
req = requests.get(url,headers=headers)
html_content = req.text
soup = BeautifulSoup(html_content, "html.parser")

#data_get___
prod_barcode = soup.find('div', class_ = 'badge product-code badge-product-code').text
for caractere in prod_barcode:
    if caractere.isdigit():
        ean_13 += caractere

prod_title = soup.find('h1', class_ = 'product-title align-left color-text').text.replace('\n', '')

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

#find_real__
for linha in linhas_texto.split('\n'):
    if palavra_chave in linha:
        match = re.search(padrao_real, linha)
        if match:
            preco = match.group()
            valor_real.append(preco)
            contador += 2
            if contador >=2:
                break

#find_centavo__
for linha in linhas_texto.split('\n'):
    if palavra_chave in linha:
        match = re.search(padrao_centavo, linha)
        if match:
            preco = match.group()
            valor_centavo.append(preco)
            contador += 1
            if contador >=4:
                centavos = valor_centavo[1]
                break

#adjust_price__ 
preco_atual =','.join(valor_real)
preco_atual = (preco_atual + centavos).replace('.', ',')
preco_antigo =','.join(valor_real)
preco_antigo = (preco_antigo + centavos).replace('.',',')

#create_data_base__
with open(nome_arquivo, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([preco_antigo])

with open(nome_arquivo, 'r') as file:
    preco_salvo = file.read().strip().replace('"','')

os.remove(nome_arquivo)

product = {'LM': [ean_13],
        'Title': [prod_title],
        'Price': [preco_atual]}

dados = pd.DataFrame(product)
dados.to_csv('produto.csv', index= False, encoding= 'utf-8', sep= ';')


#show_code__
print(f'Código: {ean_13}\n'
       f'Título: {prod_title}\n'
       f'Preco atual: {preco_atual}\n'
       f'Preco antigo: {preco_salvo}')

verifica_preco(preco_atual, preco_salvo)
