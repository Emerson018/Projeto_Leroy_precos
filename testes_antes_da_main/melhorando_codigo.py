from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import customtkinter as ctk
import time
from bs4 import BeautifulSoup
import requests


def get_url(lm_cliente):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    chrome_options = Options()
    #chrome_options.add_argument('--headless') pra funcionar sem abrir o programa
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.leroymerlin.com.br/')
    driver.implicitly_wait(5)

    time.sleep(3)
    troca_regiao = driver.find_element(By.XPATH,
                            '//*[@id="radix-:r5:"]/div/div/div/button[1]').click()
    time.sleep(1)
    seleciona_cep = driver.find_element(By.XPATH,
                            '//*[@id="field-backyard-ui-:rl:"]').send_keys('90810240')
    time.sleep(1)
    seleciona_cdd = driver.find_element(By.XPATH,
                            '//*[@id="radix-:r2:"]/form/button').click()
    time.sleep(1)
    input_lm = driver.find_element(By.XPATH,
                            '//*[@id="autocomplete-0-input"]')
    time.sleep(1)
    input_lm.send_keys(lm_cliente)
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
    print(ean_13)



ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

window = ctk.CTk()
window.title('Preços Leroy Merlin')
window.geometry('800x500')


def fecha_programa():
    window.destroy()

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

def mostr_msg_erro():
    label2 = ctk.CTkLabel(
        master=frame,
        text= 'Procura LM',
        font=font_label,
        )
    label2.pack(
        pady=12,
        padx=10,
        side= 'left'
        )

    
window.mainloop()

