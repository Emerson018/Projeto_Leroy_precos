from bs4 import BeautifulSoup
import requests
import re
import csv
import datetime
import os


def ajusta_info(infos):

    if infos is not None:
        informacao = infos.find_next('td').text

    else:
        informacao = '---'

    return print(informacao)


def find_price(prod_price):

    linhas_texto = ''
    data_hora = datetime.datetime.now()
    nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"

    # Write_archive__
    with open(nome_arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(prod_price)

    # Read_archive__
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            linhas_texto = linhas_texto + '.'.join(row) + '\n'

    default = r"const integers = '([\d.]+)'"

    values = []

    for line in linhas_texto.split('\n'):
        match = re.search(default, line)
        if match:
            price = match.group()
            values.append(price)

    elemento = values[0]
    valor = elemento.split("'")[1]

    os.remove(nome_arquivo)

    return valor


# app_action___
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = "https://www.leroymerlin.com.br/banheira-de-imersao-zen-150x72cm-branco-sensea_91989296"

req = requests.get(
    url,
    headers=headers
)

html_content = req.text
soup = BeautifulSoup(
    html_content,
    "html.parser"
)

prod_price = soup.find(
    'div',
    class_='product-price-tag'
)

span_tag = soup.find(
    'div',
    {'data-product-pice-tag'}
)

info = soup.find(
    'div',
    class_='product-info-details'
)


infos_produto = [
    'Produto',
    'Dimensão',
    'Cor',
    'Modelo',
    'Marca',
    'Garantia do Fabricante'
    'teste'
]

# ajusta a informação dos produtos para cada dado contido dentro da lista informações
# dos produtos se os dados não forem None.
dados = [ajusta_info(info.find('th', string=dado)) for dado in infos_produto]


linhas_texto = find_price(prod_price)

print(linhas_texto)

# DESCOBRIR O QUE SAO
# API
# FRAMEWORK
