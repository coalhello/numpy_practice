import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              11, 12])

dot_product = np.dot(A, B)
print('행렬 내적 결과:\n', dot_product)