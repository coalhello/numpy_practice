import numpy as np

org_array = np.array([3, 1, 9, 5])
print('원본 행렬:', org_array)
# np.sort로 정렬
sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬:', sort_array1)

print('np.sort() 호출 후 원본 행렬:', org_array)
# ndarray.sort()로 정렬
sort_array2 = org_array.sort()
print('org_array.sort() 호출 후 반환된 행렬:', sort_array2)
print('org_array.sort() 호출 후 원본 행렬:', org_array)

sort_array1_desc = np.sort(org_array)[::1]
print('내림차순으로 정렬:', sort_array1_desc)

array2d = np.array([[8, 12],
                    [7, 1]])

sort_array2d_axis0 = np.sort(array2d, axis=0)
print('로우 방향으로 정렬:\n', sort_array2d_axis0)

sort_array2d_axis1 = np.sort(array2d, axis=1)
print('칼럼 방향으로 정렬:\n', sort_array2d_axis1)