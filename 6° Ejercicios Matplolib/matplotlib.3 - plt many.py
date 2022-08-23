import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])


x3 = np.array([5, 2, 2, 10])
y3 = np.array([9, 7, 5, 1])

x4 = np.array([1, 3, 2, 3])
y4 = np.array([1, 2, 3, 1])

plt.plot(x1, y1, x2, y2, x3, y3, x4, y4)
plt.show()