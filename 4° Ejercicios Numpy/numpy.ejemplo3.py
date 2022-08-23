import numpy as np


#Matriz de 1 Dimensiones
arr1 = np.array([0, 1.3, 2, 3, 4, 5, 6, 7, 8, "9a"])
#print(arr1)
#print(arr1.dtype)

arr2 = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
#print(arr2)
#print(arr2.shape)

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(arr3)
print(arr3.reshape(3,5))