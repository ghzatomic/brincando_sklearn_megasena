import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

# Substitua pelo caminho real do seu arquivo CSV
caminho_do_arquivo = 'mega_sena_asloterias_ate_concurso_2669_sorteio.csv'

# Carregar os dados
df = pd.read_csv(caminho_do_arquivo)

# Supondo que 'Concurso' é o número do sorteio
X = df[['Concurso']]  # Aqui você pode adicionar mais características
y = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']].apply(lambda row: set(row), axis=1)

# Transformação para formato binário
mlb = MultiLabelBinarizer(classes=range(1, 61))
y_mlb = mlb.fit_transform(y)

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_mlb, test_size=0.2, random_state=42)

# Modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Previsões para o próximo concurso
ultimo_concurso = df['Concurso'].iloc[-1] + 1
novo_sorteio = pd.DataFrame({'Concurso': [ultimo_concurso]})

# Gera probabilidades para cada número
probabilidades = modelo.predict_proba(novo_sorteio)

# Gera 10 conjuntos de previsões aleatórias
for i in range(10):
    previsao = set()
    while len(previsao) < 6:
        for j in range(60):  # Iterando sobre os 60 números possíveis
            prob = probabilidades[j][0, 1]  # Acessando a probabilidade do número ser escolhido
            if np.random.rand() < prob:
                previsao.add(j + 1)
            if len(previsao) == 6:
                break
    print(f"Previsão {i+1} para o sorteio {ultimo_concurso}: {sorted(previsao)}")