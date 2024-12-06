# -*- coding: utf-8 -*-
"""Delaunay/Voronoi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XaD4mYRKH_7LmStEVe3XMft2laBfHK9E

Creating a set of 2D points:
"""

import random
import numpy as np

'''list_ = []
for i in range(100):
  point_x, point_y = random.uniform(0,100), random.uniform(0,100)
  list_.append(tuple([point_x,point_y]))

matriz_pontos = np.column_stack([
    np.random.uniform(low, high, n_pontos) for low, high in dimensoes
'''

dimensoes = [
    (0, 100),  # Intervalo para x
    (0, 100), # Intervalo para y
]

# Número de pontos
n_pontos = 100

# Gerar os arrays uniformes para cada dimensão e empilhá-los
matriz_pontos = np.column_stack([
    np.random.uniform(low, high, n_pontos) for low, high in dimensoes #pega as matrizes criadas pelos arrays uniformes e junta em uma matriz
])

"""Calculating Delaunay Triangulation and Voronoi:"""

from scipy.spatial import Delaunay, Voronoi
dela = Delaunay(matriz_pontos) #magia do scipy eba
vorono = Voronoi(matriz_pontos)

"""Visualization with MatPlotLib"""

import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d
fig = voronoi_plot_2d(vorono, show_vertices=False)
plt.triplot(matriz_pontos[:,0], matriz_pontos[:, 1], dela.simplices)
plt.plot(matriz_pontos[:,0], matriz_pontos[:, 1], 'o')
plt.show()