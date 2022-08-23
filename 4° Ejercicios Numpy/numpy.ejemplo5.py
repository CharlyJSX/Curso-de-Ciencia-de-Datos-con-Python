import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
#[1 2 3 4 5 6]
print(arr3)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.array_split(arr4, 3)
print(newarr)


arr5 = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr5 == 4)
print(x)


arr6 = np.array([3, 2, 0, 1])
print(np.sort(arr6))

arr = np.array([41, 42, 43, 44])
x = arr[[True, False, True, False]]
print(x)