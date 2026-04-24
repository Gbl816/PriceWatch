import requests
from bs4 import BeautifulSoup

def pegar_preco(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    preco = soup.find('span', class_='price')

    if preco:
        return preco.text.strip()
    
    return None