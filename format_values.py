import re

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