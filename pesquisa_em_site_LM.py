from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

#Chrome_options__
chrome_options = Options()
#chrome_options.add_argument('--headless') pra funcionar sem abrir o programa
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#get_url__
driver.get('https://www.leroymerlin.com.br/')

#find_url__
'''
search1 = driver.find_element(By.XPATH,
     "//*[contains(@class, 'aE8V9') and contains(@class, 'htek1') and contains(@class, 'C0tWl')]")
search1.send_keys('91697550')
search1.send_keys(Keys.ENTER)
'''
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
input_lm.send_keys('91697550')
input_lm.send_keys(Keys.ENTER)

time.sleep(3)
get_title = driver.find_element(By.XPATH,
                            '/html/body/div[11]/div/div[1]/div[1]/div/div[1]/h1').text
print(get_title)
