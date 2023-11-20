import numpy as np
from scipy.stats import multivariate_normal

def log_density(X, m, C):
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    N, D = X.shape
    const = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    deviations = X - m
    exponents = -0.5 * np.sum(deviations @ inv_C * deviations, axis=1)
    return const + exponents

m = np.array([1, 2])
C = np.array([[2, 0.5], [0.5, 1]])
X = np.array([[1, 2], [2, 3], [3, 4]])


result_custom = log_density(X, m, C)
result_scipy = multivariate_normal(m, C).logpdf(X)


print("Результаты с использованием numpy:")
print(result_custom)
print("Результаты с использованием scipy:")
print(result_scipy)

print("Результаты совпадают:", np.allclose(result_custom, result_scipy))
