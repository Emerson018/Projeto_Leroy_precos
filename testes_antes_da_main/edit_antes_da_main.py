from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os

#functions__
def add_values_to_excel(dados):
    dados = pd.DataFrame(product)

    df1 = pd.read_excel('teste.xlsx')
    existing_lm_values = df1['LM'].dropna().tolist()

    new_lm_values = dados['LM'].tolist()
    values_to_add = [lm for lm in new_lm_values if lm not in existing_lm_values]

    if values_to_add:
        dados_to_add = dados[dados['LM'].isin(values_to_add)]
        with pd.ExcelWriter(
                            'teste.xlsx',
                            mode='a',
                            engine= 'openpyxl',
                            if_sheet_exists='overlay'
                            ) as writer:
            
            dados_to_add.to_excel(
                        writer,
                        sheet_name='Sheet1',
                        header= None,
                        startrow=writer.sheets['Sheet1'].max_row,
                        index=False
                        )
        print('valores adicionados com sucesso!')

def format_real(text_lines):
    key_word = 'const'
    default = r'\d+\.\d{3}|\d.\d{2}'
    values = []
    counter = 0

    for line in text_lines.split('\n'):
        if key_word in line:
            match = re.search(default, line)
            if match:
                price = match.group()
                values.append(price)
                counter +=2
                if counter >=2:
                    break

    price_now =','.join(values)
    return price_now

def format_cents(text_lines):
    key_word = 'const'
    default = r'.\d{2}'
    values = []
    counter = 0

    for line in text_lines.split('\n'):
        if key_word in line:
            match = re.search(default, line)
            if match:
                price = match.group()
                values.append(price)
                counter +=1
                if counter >=4:
                    cents_value = values[1]
                    break
    
    return cents_value

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

#variables__
ean_13 = ''

url = input('Digite o link: ')
#app_action___
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
#url = "https://www.leroymerlin.com.br/ar-condicionado-split-24000-btus-quente-e-frio-220v-series-a1-tcl_91697550?term=91697550&searchTerm=91697550&searchType=LM"
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

#call_functions__

linhas_texto = find_price(prod_price)
reais = format_real(linhas_texto)
centavos = format_cents(linhas_texto)

#adjust_price__ 
reais = (reais + centavos).replace('.', ',',2)

#create dict__
product = {'LM': [ean_13],
        'Title': [prod_title],
        'Price': [reais]}

add_values_to_excel(product)

print(
    'Os seguintes valores foram adicionados:\n\n'
    f'Código: {ean_13}\n'
    f'Título: {prod_title}\n'
    f'Preco atual: {reais}')


#tentar fazer com que o programa econtre qualquer valor ao inves de valores acima de R$1.000