import re

def format_real(text_lines):
    default = r"data-price='{\"integers\":\"([\d.]+)\",\"decimals\":\"([\d]+)\"}'"
    matches = re.search(default, text_lines)
    if matches:
        integers, decimals = matches.groups()
        price = f"{integers.replace('.','')}.{decimals}"

    return price

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

def format_data(reais, ean_13, title):
    # format_price__
    preco = reais

    # format_data__
    product = {'LM': [int(ean_13)],
               'Title': [str(title)],
               'Price': [float(preco)]}
    produtos_csv = [ean_13, title, preco]

    return product, produtos_csv, preco

def format_info(infos):
    if infos is not None:
        informacao = infos.find_next('td').text
    else:
        informacao = '---'

    return print(informacao)