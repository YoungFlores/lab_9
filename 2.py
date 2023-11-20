import numpy as np

def run_length_encoding(x):
    unique_elements, counts = np.unique(x, return_counts=True)
    return unique_elements, counts

x = np.array([2, 2, 2, 3, 3, 3, 5])
result = run_length_encoding(x)
print(result)