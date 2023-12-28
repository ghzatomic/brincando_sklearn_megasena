import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

# Substitua pelo caminho real do seu arquivo CSV
caminho_do_arquivo = 'mega_sena_asloterias_ate_concurso_2669_sorteio.csv'

# Carregar os dados
df = pd.read_csv(caminho_do_arquivo)

X = df[['Concurso']]
y = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']].apply(lambda row: set(row), axis=1)

# Transformar os rótulos em um formato binário
mlb = MultiLabelBinarizer(classes=range(1, 61))  # Supondo que os números vão de 1 a 60
y_mlb = mlb.fit_transform(y)

# Dividir os dados em conjunto de treino e teste
# X pode ser um conjunto de características derivadas dos dados, como estatísticas dos sorteios anteriores
X_train, X_test, y_train, y_test = train_test_split(X, y_mlb, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Prever os números de um possível próximo sorteio
# Aqui, vamos usar algumas características dos últimos sorteios como entrada

#novo_sorteio = pd.DataFrame({'Concurso': [df['Concurso'].iloc[-1] + 1]})
#previsao = modelo.predict(novo_sorteio)
#numeros_previstos = mlb.inverse_transform(previsao)

#ultimo_concurso = df['Concurso'].iloc[-1]
#for i in range(1, 11):
#    novo_sorteio = pd.DataFrame({'Concurso': [ultimo_concurso + i]})
#    previsao = modelo.predict(novo_sorteio)
#    numeros_previstos = mlb.inverse_transform(previsao)
#    print(f"Números previstos para o sorteio {novo_sorteio['Concurso'].iloc[0]}: {numeros_previstos[0]}")


# Previsões para o próximo concurso
ultimo_concurso = df['Concurso'].iloc[-1] + 1
novo_sorteio = pd.DataFrame({'Concurso': [ultimo_concurso]})

# Gera probabilidades para cada número
probabilidades = modelo.predict_proba(novo_sorteio)

# Gera 10 conjuntos de previsões aleatórias
for i in range(10):
    previsao = []
    for prob in probabilidades:
        previsao.append(np.random.choice(np.arange(1, 61), p=prob/prob.sum()))
    previsao = set(previsao)  # Remove duplicatas se houver
    print(f"Previsão {i+1} para o sorteio {ultimo_concurso}: {previsao}")


