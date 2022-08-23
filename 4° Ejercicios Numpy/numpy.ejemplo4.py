import numpy as np

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

arr4 = arr3.reshape(3,5)
print(arr4)

i = 0
j = 0
for x in arr4:
    i += 1
    print("Matriz",i," :", x)

    for y in x:
        j += 1
        print("Posición ",i,",",j," :", y)

    j = 0

print(arr3)
for x in np.nditer(arr4):
    print(x)

