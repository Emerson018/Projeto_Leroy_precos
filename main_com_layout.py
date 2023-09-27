from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv
import datetime
import os
import customtkinter as ctk


# functions__
def get_url(url):
    # app_action___
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(
        url,
        headers=headers
    )
    html_content = req.text
    soup = BeautifulSoup(
        html_content,
        "html.parser"
    )
    return soup


def check_values(ean, file_name):
    # df = pd.read_csv(file_name, encoding='latin-1')
    with open(file_name, newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        encontrou = False

        for linha in leitor:
            if ean in linha[0]:
                encontrou = True
                break

        if encontrou:
            print('VALORES JÁ EXISTENTES.')
        else:
            print
            add_values_to_excel(product)
            add_values_to_csv(produtos_csv, nome_arquivo_csv)
            print(
                'Os seguintes valores foram adicionados:\n\n'
                f'Código: {ean_13}\n'
                f'Título: {title}\n'
                f'Preco atual: R${preco}')


def add_values_to_csv(dados, nome_arquivo):

    with open(nome_arquivo, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dados)


def add_values_to_excel(dados):
    dados = pd.DataFrame(product)

    df1 = pd.read_excel('teste.xlsx')
    existing_lm_values = df1['LM'].dropna().tolist()

    new_lm_values = dados['LM'].tolist()
    values_to_add = [
        lm for lm in new_lm_values if lm not in existing_lm_values]

    if values_to_add:
        dados_to_add = dados[dados['LM'].isin(values_to_add)]
        with pd.ExcelWriter(
            'teste.xlsx',
            mode='a',
            engine='openpyxl',
            if_sheet_exists='overlay'
        ) as writer:

            dados_to_add.to_excel(
                writer,
                sheet_name='Sheet1',
                header=None,
                startrow=writer.sheets['Sheet1'].max_row,
                index=False
            )


def format_real(text_lines):

    default = r"const integers = '([\d.]+)'"
    values = []

    for line in text_lines.split('\n'):
        match = re.search(
            default,
            line
        )
        if match:
            price = match.group()
            values.append(price)

    value = values[0].split("'")[1]
    return value


def format_cents(text_lines):
    key_word = 'const'
    default = r'.\d{2}'
    values = []
    counter = 0

    for line in text_lines.split('\n'):
        if key_word in line:
            match = re.search(
                default,
                line
            )
            if match:
                price = match.group()
                values.append(price)
                counter += 1
                if counter >= 4:
                    cents_value = values[1]
                    break

    return cents_value


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


def format_data(reais, centavos):
    # format_price__
    preco = (reais + centavos)

    # format_data__
    product = {'LM': [str(ean_13)],
               'Title': [str(title)],
               'Price': [preco]}
    produtos_csv = [ean_13, title, preco]

    return product, produtos_csv, preco


def ajusta_info(infos):
    if infos is not None:
        informacao = infos.find_next('td').text
    else:
        informacao = '---'

    return print(informacao)


def main():

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')
    window = ctk.CTk()
    window.title('Database Leroy')
    window.geometry('800x500')

    frame = ctk.CTkFrame(master=window)
    frame.pack(
        pady=20,
        padx=60,
        fill='both',
        expand=True
    )

    font_label = ctk.CTkFont(
        family='Calibri',
        size=24,
        weight='bold'
    )

    label = ctk.CTkLabel(
        master=frame,
        text= 'Procura LM',
        font=font_label,
    )
    label.pack(
        pady=12,
        padx=10
    )

    entry1 = ctk.CTkEntry(
        master=frame,
        placeholder_text='Insira o LM aqui'
    )
    entry1.pack(
        pady=12,
        padx=10
    )
    search_lm_button = ctk.CTkButton(
        master=frame,
        text='Validar preço',
        command=lambda: get_url(entry1.get())
    )
    search_lm_button.pack(
        pady=12,
        padx=10
    )

    text = ctk.CTkTextbox(
        master= frame,
        width= 300, #numero de caracteres/linha
        height= 200  #qntd de linhas
    )
    text.pack()

    button_exit = ctk.CTkButton(
        master=window,
        text ='Fechar programa',
        command=window.destroy
        )
    button_exit.pack(
        side='bottom',
        padx=10,
        pady=10,
        anchor='se'
        )
    
    button_add_excel = ctk.CTkButton(
        master= frame,
        text= 'Add ao banco de dados'
        #command= lambda: 
    )
    button_add_excel.pack(
        side='bottom',
        padx=10,
        pady=10,
    )
        
    window.mainloop()

# Main__
soup = get_url()
# get_data__
nome_arquivo_csv, title, prod_price, ean_13, infos, infos_produto = data_get(
    soup)
# find_price__
linhas_texto = find_price(prod_price)
# format_price__
reais = format_real(linhas_texto)
centavos = format_cents(linhas_texto)
# format_data__
product, produtos_csv, preco = format_data(reais, centavos)
# check_data__
check_values(ean_13, nome_arquivo_csv)
# save_data__


dados = [ajusta_info(infos.find('th', string=dado)) for dado in infos_produto]

# só nao ta encontrando valroes abaixo de 10 reais
