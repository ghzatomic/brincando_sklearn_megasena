import pandas as pd
import matplotlib.pyplot as plt

# Supondo que você tenha um arquivo CSV com uma coluna para cada número sorteado
# Exemplo: colunas 'num1', 'num2', 'num3', 'num4', 'num5', 'num6' em 'megasena.csv'
df = pd.read_csv('caminho_para_o_arquivo/megasena.csv')

# Extrai todos os números sorteados em uma única série
numeros_sorteados = pd.concat([df['num1'], df['num2'], df['num3'], df['num4'], df['num5'], df['num6']], ignore_index=True)

# Conta a frequência de cada número
frequencia_numeros = numeros_sorteados.value_counts()

# Plota a frequência dos números
plt.figure(figsize=(12,6))
frequencia_numeros.sort_index().plot(kind='bar')
plt.title('Frequência dos Números Sorteados na Mega-Sena')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.show()