import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([1, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

print()
print(csr_matrix(arr.data))

print()
print(csr_matrix(arr).count_nonzero())
