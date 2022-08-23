import numpy as np

#Matriz de 0 Dimensiones
arr0 = np.array(0)
print(arr0)
print(arr0.ndim, "\n")

#Matriz de 1 Dimensiones
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.ndim, "\n")

#Matriz de 2 Dimensiones
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) 
print(arr2) 
print(arr2.ndim, "\n")

#Matriz de 3 Dimensiones
arr3 = np.array([[[1, 2, 3], [4, 5, 6] ] , [[1, 2, 3], [4, 5, 6 ]]])
print(arr3)
print(arr3.ndim, "\n")

#Matriz de 6 Dimensiones
arr6 = np.array([1, 2, 3, 4], ndmin=6)
print(arr6)
print(arr6.ndim, "\n")