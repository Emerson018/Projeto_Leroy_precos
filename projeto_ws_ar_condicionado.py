from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os

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

#==== A PARTIR DAQUI MODIFICR O PROD_PRICE PRA DIMINUIR A QUANTIDADE DE CARACTERES====

#Write_archive__
with open(nome_arquivo, 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(prod_price)

#Read_archive__
with open(nome_arquivo, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        linhas_texto = linhas_texto + ','.join(row) + '\n'

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
valores_str =','.join(valores)

product = {'LM': [prod_barcode],
        'Title': [prod_title],
        'Price': [valores_str]}

dados = pd.DataFrame(product)
dados.to_csv('produto.csv', index= False, encoding='utf-8', sep=';')

print(f"Arquivo criado: {nome_arquivo}")

'''
todos sao do tipo STR
print(prod_barcode) 
print(prod_title)
print(valores_str)
#ctrl + ';' comenta a linha 
'''
'''
===basico===
>>> limpar o arquivo csv antes de salvá-lo, tirando espaços em branco(.strip) e removendo linhas que não serão usadas.
>>> Organizar ele com o chat gpt mostrou.
>>> tentar adicionar FUNÇÕES.

===avançado===
>>> criar um banco de dados com os links dos ar condicionados. salsd
>>> fazer com q a o banco de dados mostre os preços que alteraram com o tempo.
'''