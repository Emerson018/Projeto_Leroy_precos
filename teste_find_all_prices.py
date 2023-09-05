from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os

def find_price(prod_price):

    linhas_texto = ''
    data_hora = datetime.datetime.now()
    nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"
    
    #Write_archive__
    with open(nome_arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(prod_price)

    #Read_archive__
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            linhas_texto = linhas_texto + '.'.join(row) + '\n'

    os.remove(nome_arquivo)

    return linhas_texto


def format_real(text_lines):
   

    #lines = text_lines.split('\n')

    asd = text_lines
    #for line in lines:
        #valores_numericos = re.findall(r'\d+\.\d+|\d+', text_lines)

    #for _ in range(1):
        #next(valores_numericos)


    return asd


url = input('Digite o link: ')
#app_action___
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
#url = "https://www.leroymerlin.com.br/ar-condicionado-split-24000-btus-quente-e-frio-220v-series-a1-tcl_91697550?term=91697550&searchTerm=91697550&searchType=LM"
req = requests.get(url,headers=headers)
html_content = req.text
soup = BeautifulSoup(html_content, "html.parser")

prod_price = soup.find('div', class_= 'product-price-tag')

linhas_texto = find_price(prod_price)
real = format_real(linhas_texto)

print(real)

