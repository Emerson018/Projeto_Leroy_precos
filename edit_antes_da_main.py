from bs4 import BeautifulSoup
import requests
from save_data import execute_query, create_db_connection, check_values
from format_values import format_real, format_cents, format_data, format_info
from search_data import find_price, data_get


def main():
    # app_action___
    url = input('Digite o link: ')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(url,headers=headers)
    html_content = req.text
    soup = BeautifulSoup(html_content,"html.parser")

    return soup


# Main__
soup = main()
# get_data__
nome_arquivo_csv, title, prod_price, ean_13, infos, infos_produto = data_get(
    soup)
# find_price__
linhas_texto = find_price(prod_price)
# format_price__
reais = format_real(linhas_texto)
centavos = format_cents(linhas_texto)
# format_data__
product, produtos_csv, preco = format_data(reais, centavos, ean_13, title)
# check_data__
check_values(ean_13, nome_arquivo_csv, title, product, produtos_csv, nome_arquivo_csv, preco)
# save_data__


dados = [format_info(infos.find('th', string=dado)) for dado in infos_produto]

pw = 'mano34835965'
db = 'db_leroy'


dados_db = (ean_13, title, preco)
# (lm, title, price)

informacoes_do_produto = """
INSERT INTO products (lm, title, price) VALUES
(%s, %s, %s);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, informacoes_do_produto,dados_db)



# só nao ta encontrando valroes abaixo de 10 reais

#O CÓDIGO FUNCIONA, MAS TEM Q COLOCAR O 'FROM IMPORT' DENTRO DA FUNÇÃO
#PRA ELA NAO RODAR PRIMEIRO QUE O CODIGO MAIN.
# O PROGRAMA TA RODANDO COM OS VALORES DO 'INSERT_VALUES_DB' AO INVES
#DESSE DAQUI.