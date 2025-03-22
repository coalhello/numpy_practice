import numpy as np

# 단일 값 추출

# 1부터 9까지의 1차원 ndarray 생성
array1 = np.arange(start=1, stop=10)
print('array1:', array1)

# index는 0부터 시작하므로  array1[2]는 3번째 위치 데이터 의미
value = array1[2]
print("value:", value)
print(type(value))

print('맨 뒤의 값:', array1[-1], '맨 뒤에서 두 번째 값:', array1[-2])

array1[0] = 9
array1[8] = 0
print('array1:', array1)

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)

print('(row=0, col=0) index 가리키는 값:', array2d[0, 0])
print('(row=0, col=1) index 가리키는 값:', array2d[0, 1])
print('(row=1, col=0) index 가리키는 값:', array2d[1, 0])
print('(row=2, col=2) index 가리키는 값:', array2d[2, 2])

# 슬라이싱

array1 = np.arange(start=1, stop=10)
array3 = array1[0:3]
print(array3)
print(type(array3))

array1 = np.arange(start=1, stop=10)
array4 = array1[:3]
print(array4)

array5 = array1[3:]
print(array5)

array6 = array1[:]
print(array6)

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print('array2d:\n', array2d)

print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
print('array[1:3, :] \n', array2d[1:3, :])
print('array2d[:, :] \n', array2d[:, :])
print('array2d[:2, :1] \n', array2d[:2, 1:])
print('array2d[:2, 0] \n',  array2d[:2, 0])

print(array2d[0])
print((array2d[1]))
print('array2d[0] shpae:', array2d[0].shape, 'array2d[1] shape:', array2d[1].shape)