import pandas as pd
import csv
from csv import writer
from csv import DictWriter

prod_barcode = 'Émerson'
prod_title = 't`este'
valores_str = 'Viçsa'

product = {
        'LM': [],
        'Title': [],
        'Price': []
        }

product['LM'].append(prod_barcode)
product['Title'].append(prod_title)
product['Price'].append(valores_str)


dados = pd.DataFrame(product)
dados.to_csv('produto.csv', index= False, encoding='utf-8', sep=';')

'''
field_names = ['LM', 'Title', 'Price']
dict = {
        'LM': 4444,
        'Title': 'Teste',
        'Price': 1212
        }


with open ('produto.csv', 'a', newline= '') as arquivo:
    writer_object = DictWriter(arquivo, fieldnames=field_names)
    writer_object.writerow(dict)
    arquivo.close()
'''