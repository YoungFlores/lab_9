import numpy as np


random_array = np.random.randn(10, 4)


min_value = np.min(random_array)
max_value = np.max(random_array)
mean_value = np.mean(random_array)
std_deviation = np.std(random_array)


first_five_rows = random_array[:5, :]

print(f"Минимальное значение: {min_value}")
print(f"Максимальное значение: {max_value}")
print(f"Среднее значение: {mean_value}")
print(f"Стандартное отклонение: {std_deviation}")
print(f"Первые 5 строк:\n{first_five_rows}")