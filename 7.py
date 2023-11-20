import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Получаем уникальные значения и их количество в столбце species
unique_species, counts = np.unique(iris[:, -1], return_counts=True)

print("Уникальные значения в столбце species:", unique_species)
print("Количество каждого значения:", counts)
