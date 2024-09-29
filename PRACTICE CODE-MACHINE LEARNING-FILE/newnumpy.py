import numpy as np
import sys

var = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("jumlah memori oleh sys : ", sys.getsizeof(var) * len(var))
print("jumlah memori oleh numpy: ", matriks.size * matriks.itemsize)

print(matriks[2][1])

def_mat = np.array([[1, 2], [3, 4]])

result = def_mat * 2
print(result)
