import mysql.connector
from mysql.connector import Error
import pandas as pd
import csv


def create_db_connection(host_name, user_name, user_pass, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_pass,
            database = db_name
        )
        print('MySQL DB connection successfull!')
    except Error as err:
        print(f"Error: '{err}")
    return connection


def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print('Query was successful!')
    except Error as err:
        print(f"Error: '{err}'")


def check_values(ean_13, file_name, title, product, produtos_csv, nome_arquivo_csv, preco):

    with open(file_name, newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        encontrou = False

        for linha in leitor:
            if ean_13 in linha[0]:
                encontrou = True
                break

        if encontrou:
            print('VALORES JÁ EXISTENTES.')
        else:
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
    dados = pd.DataFrame(dados)

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
