import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Base de dados: [Cenas de Ação, Cenas de Romance]
filmes = [
    [15, 2], # Ação 1
    [12, 4], # Ação 2 
    [4, 15], # Romance 1
    [2, 14]  # Romance 2
]
generos = ['Ação', 'Ação', 'Romance', 'Romance']

# Criação e treinamento do modelo KNN (K=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(filmes, generos)


novo_filme = [[10, 10]] 
resultado = knn.predict(novo_filme)
print(f"Resultado KNN: O filme foi classificado como {resultado[0]}")


# PLOTAGEM 

plt.figure(figsize=(8, 6))

plt.scatter([15, 12], [2, 4], color='blue', label='Ação', s=100)
plt.scatter([4, 2], [15, 14], color='deeppink', label='Romance', s=100)

novo_x = novo_filme[0][0]
novo_y = novo_filme[0][1]

plt.scatter(novo_x, novo_y, color='orange', marker='*', s=200, label=f'Misterioso [{novo_x}, {novo_y}]')

plt.annotate('Ação 1', (15, 2), textcoords="offset points", xytext=(0,-15), ha='center')
plt.annotate('Ação 2', (12, 4), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate('Romance 1', (4, 15), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate('Romance 2', (2, 14), textcoords="offset points", xytext=(0,-15), ha='center')

plt.title('Classificação KNN - Ação vs Romance')
plt.xlabel('Cenas de Ação')
plt.ylabel('Cenas de Romance')
plt.xlim(0, 18)
plt.ylim(0, 18)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()