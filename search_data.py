import datetime
import csv
import os
from io import StringIO

def find_price(prod_price):

    linhas_texto = []
    data_hora = datetime.datetime.now()
    nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"

    # Write_archive__
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerows(prod_price)

    buffer.seek(0)
    reader = csv.reader(buffer)

    for row in reader:
        linhas_texto.append('.'.join(row))

    return '\n'.join(linhas_texto)

def data_get(soup):
    ean_13 = ''
    nome_arquivo_csv = "dados.csv"

    prod_barcode = soup.find(
        'div',
        class_='badge product-code badge-product-code'
    ).text

    for caractere in prod_barcode:
        if caractere.isdigit():
            ean_13 += caractere

    title = soup.find(
        'h1',
        class_='product-title align-left color-text'
    ).text.replace('\n', '')

    prod_price = soup.find(
        'div',
        class_='product-price-tag'
    )
    infos = soup.find(
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
        'teste',
        'Tipo',
        'Potencia',
        'Tipo de Ar Condicionado']

    return nome_arquivo_csv, title, prod_price, ean_13, infos, infos_produto