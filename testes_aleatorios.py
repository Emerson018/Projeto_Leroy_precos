from bs4 import BeautifulSoup
import requests
import re
import random
url = input('Insira o link: ')
url2 = 'https://www.google.com.br/search?q='

def requisition(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(url,headers=headers)
    html_content = req.text
    soup = BeautifulSoup(html_content,"html.parser")

    return soup
'''
def random_int():
    return random.randint(1, 40)

def random_float():
    return round(random.uniform(2.0,4.8),1)

# barcode__
ean_13 = ''
prod_barcode = requisition(url).find('div',class_='badge product-code badge-product-code').text
for caractere in prod_barcode:
    if caractere.isdigit():
        ean_13 += caractere

# raiting__
concat_url = url2 + ean_13 + '+leroy+merlin'
get_info = requisition(concat_url).find('div', class_='fG8Fp uo4vr').text

avalia = re.search(r'Avaliação: (\d,\d+)', get_info)
comentario = re.search(r'(\d+) comentários', get_info)
if avalia:
    avaliacao = avalia.group(1)
    media_avaliacao = comentario.group(1)
    print(f'Avaliações: {avaliacao}')
    print(f'Qnt de comentários: {media_avaliacao}')
else:
    print('Não há avaliações para esse produto')
    avaliacao = random_int()
    media_avaliacao = random_float()
    print(f'avaliações: {avaliacao} -- Média notas: {media_avaliacao}')
'''
descricao = requisition(url).find('div', class_='product-info-details')

### PEGA AS CARACTERÍSTICAS DO PRODUTO E COLOCA EM UM DICIONARIO

caracteristicas = requisition(url).find('table', class_='characteristics-table')

dicionario = {}

for linha in caracteristicas.find_all('tr'):
    chave = linha.th.text.strip()
    valor = linha.td.text.strip()
    dicionario[chave] = valor

print(dicionario)