from bs4 import BeautifulSoup
import requests

url = 'https://www.jumia.co.ke/catalog/?q=discount'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)