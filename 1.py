import numpy as np


read_matrix = np.loadtxt('matrix.txt', delimiter=',')


matrix_sum = np.sum(read_matrix)
matrix_max = np.max(read_matrix)
matrix_min = np.min(read_matrix)

print(f"Сумма элементов матрицы: {matrix_sum}")
print(f"Максимальный элемент матрицы: {matrix_max}")
print(f"Минимальный элемент матрицы: {matrix_min}")
