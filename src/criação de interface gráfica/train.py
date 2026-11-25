
import pandas as pd
import joblib

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Dados de exemplo para treinar o modelo
dados = {
    'horas_estudo': [2, 3, 5, 7, 10, 12, 15, 18, 4, 8, 14, 16],
    'faltas': [20, 15, 12, 8, 5, 3, 2, 0, 25, 10, 4, 1],
    'nota_p1': [2, 3, 4, 5, 7, 8, 9, 10, 3, 6, 8, 9],
    'situacao': [
        'Reprovado', 'Reprovado', 'Reprovado',
        'Reprovado', 'Aprovado', 'Aprovado',
        'Aprovado', 'Aprovado', 'Reprovado',
        'Aprovado', 'Aprovado', 'Aprovado'
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Separando os dados
X = df[['horas_estudo', 'faltas', 'nota_p1']]
y = df['situacao']

# Criando o modelo k-NN
modelo = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=3)
)

# Treinando o modelo
modelo.fit(X, y)

# Salvando o modelo
joblib.dump(modelo, 'modelo_desempenho.pkl')

print('Modelo treinado e salvo com sucesso!')
