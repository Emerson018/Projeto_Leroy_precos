from bs4 import BeautifulSoup
import requests

url = input('insira o link: ')
def requisition(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(url,headers=headers)
    html_content = req.text
    soup = BeautifulSoup(html_content,"html.parser")

    return soup

for item in requisition(url).find_all('img', limit=1):
    print(item['src'])