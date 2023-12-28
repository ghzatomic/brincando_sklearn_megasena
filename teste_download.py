import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL com os dados da Mega-Sena
url = 'https://www.loteriaseresultados.com.br/index.php/megasena/concurso/'

# Lista para armazenar os números sorteados
numeros_sorteados = []

# Exemplo: analisar os últimos 10 sorteios
for concurso in range(2500, 2510):
    # Obtém a página com os resultados
    page = requests.get(url + str(concurso))
    soup = BeautifulSoup(page.content, 'html.parser')

    # Encontra os números sorteados
    numeros = soup.find_all('div', class_='white--text font-weight-bold')

    # Adiciona os números à lista
    for numero in numeros:
        numeros_sorteados.append(int(numero.text))

# Conta a frequência de cada número
frequencia_numeros = pd.Series(numeros_sorteados).value_counts()

# Plota a frequência dos números
plt.figure(figsize=(12,6))
frequencia_numeros.sort_index().plot(kind='bar')
plt.title('Frequência dos Números Sorteados na Mega-Sena')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.show()