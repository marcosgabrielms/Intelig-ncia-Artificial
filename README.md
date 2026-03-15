# 🎬 Classificador de Gêneros de Filmes com KNN

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn Badge"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib Badge"/>
</p>

## 📌 Sobre o Projeto

Este projeto consiste em um modelo de aprendizado de máquina (Machine Learning) focado na classificação de filmes utilizando o algoritmo **K-Nearest Neighbors (KNN)**. O sistema prevê se um filme pertence ao gênero de **Ação** ou **Romance** com base na quantidade de cenas específicas que ele possui.

Toda a lógica foi consolidada em um único arquivo de execução (`main.py`) contendo as funções básicas do modelo e a plotagem dos dados, facilitando a compreensão direta do funcionamento do algoritmo.


## ⚙️ Funcionalidades

- **Treinamento do Modelo:** Utiliza uma base de dados pré-definida de filmes com suas respectivas contagens de cenas de ação e romance.
- **Classificação KNN:** Instancia o classificador buscando os 3 vizinhos mais próximos (`K=3`) para categorizar novos dados.
- **Previsão:** Avalia um "filme misterioso" e determina o seu gênero predominante.
- **Visualização Gráfica:** Plota o espaço de decisão utilizando a biblioteca `matplotlib` para ilustrar a dispersão dos filmes e a posição do novo dado avaliado.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Para instalar as bibliotecas necessárias, execute o comando abaixo no seu terminal:

```bash
pip install scikit-learn matplotlib