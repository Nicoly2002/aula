# Nicoly Cristina 2519155
# 5 Semestre de ADS Manha

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. CARREGAR DADOS
dados = load_iris()
X = dados.data
y = dados.target

# 2. DIVIDIR DADOS
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
) 

# 3. MODELO 1 (ÁRVORE)
modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(X_treino, y_treino)
pred_arvore = modelo_arvore.predict(X_teste)
acc_arvore = accuracy_score(y_teste, pred_arvore)

#  MODELO 2 (KNN)
modelo_knn = KNeighborsClassifier()
modelo_knn.fit(X_treino, y_treino)
pred_knn = modelo_knn.predict(X_teste)
acc_knn = accuracy_score(y_teste, pred_knn)

# 4. RESULTADOS
print("Acurácia Árvore:", acc_arvore)
print("Acurácia KNN:", acc_knn)

# 5. MATRIZ DE CONFUSÃO
matriz = confusion_matrix(y_teste, pred_arvore)
print("\nMatriz de Confusão:\n", matriz)

#6. GRÁFICOS (SUBPLOTS)
fig, ax = plt.subplots(1, 2)

# GRÁFICO 1 (ACURÁCIA)
modelos = ["Árvore", "KNN"]
valores = [acc_arvore, acc_knn]
ax[0].bar(modelos, valores)
ax[0].set_title("Comparação de Modelos")
ax[0].set_ylabel("Acurácia")
ax[0].set_ylim(0, 1)

# GRÁFICO 2 (MATRIZ)

img = ax[1].imshow(matriz)
ax[1].set_title("Matriz de Confusão")
classes = ["Setosa", "Versicolor", "Virginica"]
ax[1].set_xticks(range(len(classes)))
ax[1].set_yticks(range(len(classes)))

# ❖Coloca nomes
ax[1].set_xticklabels(classes)
ax[1].set_yticklabels(classes)

# ❖Rótulos dos eixos.
ax[1].set_xlabel("Previsto")
ax[1].set_ylabel("Real")

# NÚMEROS NA MATRIZ
for i in range(len(classes)):
    for j in range(len(classes)):
        ax[1].text(j, i, matriz[i, j], ha="center", va="center")

# BARRA DE COR
fig.colorbar(img, ax=ax[1])

# AJUSTE FINAL
plt.tight_layout()
plt.show()