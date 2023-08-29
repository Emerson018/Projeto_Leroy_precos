from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import customtkinter as ctk
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import requests
import re
import csv
import datetime
import os


def format_real(text_lines):
    key_word = 'const'
    default = r'\d+\.\d{3}|\d.\d{2}'
    values = []
    counter = 0

    for line in text_lines.split('\n'):
        if key_word in line:
            match = re.search(default, line)
            if match:
                price = match.group()
                values.append(price)
                counter +=2
                if counter >=2:
                    break

    price_now =','.join(values)
    return price_now

def format_cents(text_lines):
    key_word = 'const'
    default = r'.\d{2}'
    values = []
    counter = 0

    for line in text_lines.split('\n'):
        if key_word in line:
            match = re.search(default, line)
            if match:
                price = match.group()
                values.append(price)
                counter +=1
                if counter >=4:
                    cents_value = values[1]
                    break
    
    return cents_value

def find_price(prod_price):

    linhas_texto = ''
    data_hora = datetime.datetime.now()
    nome_arquivo = f"dados_{data_hora.strftime('%Y%m%d_%H%M%S')}.csv"

    #Write_archive__
    with open(nome_arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(prod_price)

    #Read_archive__
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            linhas_texto = linhas_texto + '.'.join(row) + '\n'

    os.remove(nome_arquivo)

    return linhas_texto

def get_url(lm_cliente):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    chrome_options = Options()
    #chrome_options.add_argument('--headless') pra funcionar sem abrir o programa
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.leroymerlin.com.br/')
    
    time.sleep(5)
    troca_regiao = driver.find_element(By.XPATH,
                            '//*[@id="radix-:r5:"]/div/div/div/button[1]').click()
    
    time.sleep(4)
    digita_cep = driver.find_element(By.XPATH,
                            '//*[@id="field-backyard-ui-:rl:"]').send_keys('90810240')
    
    time.sleep(2)
    seleciona_cdd = driver.find_element(By.XPATH,
                            '//*[@id="radix-:r2:"]/form/button').click()
    
    time.sleep(5)
    input_lm = driver.find_element(By.XPATH,
                            '//*[@id="autocomplete-0-input"]')
    
    
    input_lm.send_keys(lm_cliente)
    time.sleep(1)
    input_lm.send_keys(Keys.ENTER)
    
    
    web_link = driver.current_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(web_link,headers=headers)
    html_content = req.text
    soup = BeautifulSoup(html_content, "html.parser")

    ean_13 = ''
    prod_barcode = soup.find('div', class_ = 'badge product-code badge-product-code').text
    for caractere in prod_barcode:
        if caractere.isdigit():
            ean_13 += caractere

    prod_title = soup.find('h1', class_ = 'product-title align-left color-text').text.replace('\n', '')

    prod_price = soup.find('div', class_= 'product-price-tag')


    linhas_texto = find_price(prod_price)
    reais = format_real(linhas_texto)
    centavos = format_cents(linhas_texto)

    #adjust_price__ 
    reais = (reais + centavos).replace('.', ',',2)

    #create dict__
    product = {'LM': [ean_13],
            'Title': [prod_title],
            'Price': [reais]}
    
    produto = [ean_13,prod_title,reais]
    print(
        'Os seguintes valores foram adicionados:\n\n'
        f'Código: {ean_13}\n'
        f'Título: {prod_title}\n'
        f'Preco atual: {reais}',)

    driver.quit()

    text.insert('1.0', produto)

def fecha_programa():

    window.destroy()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

window = ctk.CTk()
window.title('Preços Leroy Merlin')
window.geometry('800x500')

frame = ctk.CTkFrame(master=window)
frame.pack(
    pady=20,
    padx= 60,
    fill= 'both',
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

    
window.mainloop()

