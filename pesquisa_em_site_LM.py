from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Chrome_options__
chrome_options = Options()
#chrome_options.add_argument('--headless') pra funcionar sem abrir o programa
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#get_url__
driver.get('https://www.leroymerlin.com.br/')
driver.implicitly_wait(5)

#find_url__
search1 = driver.find_element(By.XPATH,
     "//*[contains(@class, 'aE8V9') and contains(@class, 'htek1') and contains(@class, 'C0tWl')]")
search1.send_keys('91697550')
search1.send_keys(Keys.ENTER)

  


