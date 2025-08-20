# Importando Bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas

# Criando cabeçalho para simular navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64/ x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}
# Fazendo requisição HTTP
print('Request: ')
response = requests.get('https://webscraper.io/test-sites/tables/tables-semantically-correct', headers=headers)
print(response.text[:600])

# Interpretando o HTML com BeautifulSoup
print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

# Extraindo tabelas com Pandas
print('Pandas: ')
url_dados = pandas.read_html('https://webscraper.io/test-sites/tables/tables-semantically-correct')
print(url_dados[0].head(10))
