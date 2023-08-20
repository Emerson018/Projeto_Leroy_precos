import pandas as pd
product = {'LM': [55555],
        'Title': ['casa'],
        'Price': ['99.99']}

dados = pd.DataFrame(product)

df1 = pd.read_excel('teste.xlsx')
existing_lm_values = df1['LM'].dropna().tolist()

new_lm_values = dados['LM'].tolist()
values_to_add = [lm for lm in new_lm_values if lm not in existing_lm_values]

if values_to_add:
    dados_to_add = dados[dados['LM'].isin(values_to_add)]
    with pd.ExcelWriter(
                        'teste.xlsx',
                        mode='a',
                        engine= 'openpyxl',
                        if_sheet_exists='overlay') as writer:
        dados_to_add.to_excel(
                    writer,
                    sheet_name='Sheet1',
                    header= None,
                    startrow=writer.sheets['Sheet1'].max_row,
                    index=False)
    print('valores adicionados com sucesso!')
else:
    print('Valor já existente na planilha!')

    #AQUI TÁ DANDO UM APPEN AOS VALORES NA PLANILHA, EM CADA LINHA E COLUNA