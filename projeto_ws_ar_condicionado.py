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
ean_13 = ''
padrao = r'\d+\.\d{3}|\d,\d{2}'
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

prod_title = soup.find('h1', class_ = 'product-title align-left color-text').text.strip()

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
            if contador >=1:
                break

#print_price__
price =','.join(valores)

product = {'LM': [ean_13],
        'Title': [prod_title],
        'Price': [price]}

dados = pd.DataFrame(product)
dados.to_csv('produto.csv', index= False, encoding='utf-8', sep=';')

print("Arquivo criado!!!")
print(price)
'''
todos sao do tipo STR
print(prod_barcode) 
print(prod_title)
print(valores_str)
#ctrl + ';' comenta a linha
#com o with open n precisa fechar o arquivo 
'''
'''
===basico===
>>> limpar o arquivo csv antes de salvá-lo, tirando espaços em branco(.strip) e removendo linhas que não serão usadas.
>>> Organizar ele com o chat gpt mostrou.
>>> tentar adicionar FUNÇÕES.
>>> pra rodar sem precisar abrir um script: https://www.youtube.com/watch?v=PXMJ6FS7llk&ab_channel=freeCodeCamp.org == 1:12:00

===avançado===
>>> criar um banco de dados com os links dos ar condicionados. OU
>>> Criar um arquivo .txt com append e depois salvar ele em CSV, caso n funcione salvar direto em csv
>>> fazer com q a o banco de dados mostre os preços que alteraram com o tempo.
>>> fazer com q ele logue em POA e REGIAo
'''