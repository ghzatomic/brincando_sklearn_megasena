import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Substitua 'caminho_para_o_arquivo.csv' pelo caminho real do seu arquivo CSV
caminho_do_arquivo = 'caminho_para_o_arquivo.csv'

# Carrega os dados do arquivo CSV
df = pd.read_csv(caminho_do_arquivo)

# Extrai as colunas com os números das bolas
colunas_das_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
numeros_sorteados = df[colunas_das_bolas].values.flatten()

# Conta a frequência de cada número
frequencia_numeros = Counter(numeros_sorteados)

# Converte o contador em um DataFrame para facilitar a visualização
df_frequencia = pd.DataFrame.from_dict(frequencia_numeros, orient='index', columns=['Frequência'])
df_frequencia = df_frequencia.sort_index()

# Plota a frequência dos números
plt.figure(figsize=(15, 6))
df_frequencia['Frequência'].plot(kind='bar')
plt.title('Frequência dos Números Sorteados na Mega-Sena')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()