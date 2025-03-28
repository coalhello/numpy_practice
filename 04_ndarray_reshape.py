import numpy as np

array1 = np.arange(10)
print('array1:\n', array1)

array2 = array1.reshape(2, 5)
print('array2:\n', array2)

array3 = array1.reshape(5, 2)
print('array3\n', array3)

# array1.reshape(4, 3)

array1 = np.arange(10)
print(array1)
array2 = array1.reshape(-1, 5)
print('array2 shape:', array2.shape)
array3 = array1. reshape(5, -1)
print('array3 shape:', array3.shape)

array1 = np.arange(10)
# array4 = array1.reshape(-1, 4)

array1 = np.arange(8)
array3d = array1.reshape((2, 2, 2))
print('array3d:\n', array3d.tolist())

# 3차원 ndarray를 2차원으로 변환
array5 = array3d.reshape(-1, 1)
print('array5:\n', array5.tolist())
print('array5 shape : ', array5.shape)

# 1차원 ndarray를 2차원 ndarray로 변환
array6 = array1.reshape(-1, 1)
print('array6:\n', array6.tolist())
print('array6 shape:', array6.shape)