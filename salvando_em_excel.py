import pandas as pd

prod_barcode = 'Émerson'
prod_title = 't`este'
valores_str = 'Viçsa'

product = {'LM': [],
        'Title': [],
        'Price': []}

product['LM'].append(prod_barcode)
product['Title'].append(prod_title)
product['Price'].append(valores_str)


dados = pd.DataFrame(product)
dados.to_csv('produto.csv', index= False, encoding='utf-8', sep=';')