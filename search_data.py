import datetime
import csv
import os

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

    os.remove(nome_arquivo)

    return linhas_texto

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