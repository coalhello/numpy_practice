import numpy as np

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)

array3 = array2d[[0, 1], 2]
print('array2d[[0, 1], 2] =>', array3.tolist())

array4 = array2d[[0, 1], 0:2]
print('array2d[[0, 1, 0:2] =>', array4.tolist())

array5 = array2d[[0, 1]]
print('array2d[[0, 1] =>', array5.tolist())