#esse código funcionou para excel (xlsx)

import pandas as pd

csv_file = 'produto.csv'
excel_file = 'novos_produtos.csv'
try:
    df = pd.read_csv(csv_file)

    df.to_excel(excel_file, index= None)

    print('Arquivo convertido.')

except FileNotFoundError:
    print('arquivo csv não encontrado!!')


product = {'LM': ['984470914'],
        'Title': ['Emerson'],
        'Price': ['9999.99']}

dados = pd.DataFrame(product)

df1 = pd.read_excel('novos_produtos.xlsx')
with pd.ExcelWriter(
                    'testes.xlsx',
                    mode='a',
                    engine= 'openpyxl',
                     if_sheet_exists='overlay') as writer:
    dados.to_excel(
                    writer,
                sheet_name='Sheet1',
                header= None,
                startrow=writer.sheets['Sheet1'].max_row,
                index=False)
#mostra o valor especifico do dataframe
