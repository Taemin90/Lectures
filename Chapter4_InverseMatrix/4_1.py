'''
linalg.matrix_power(A, -1
or linalg.inv(A)

np.random.rand(3,3)
'''
import numpy as np

A = np.array([[1., 3.],
              [3., 4.]])
C = np.array([[5., 3., 2., 1.],
              [6., 2., 4., 5.],
              [7., 4., 1., 3.],
              [4., 3., 5., 2.]])
D = np.array([[4.],
             [2.],
             [5.],
             [1.]])

Ainv = np.linalg.inv(A)
print("A inverse : ", Ainv)

B = np.random.rand(3, 3)
Binv = np.linalg.inv(B)
print("B inverse : ", Binv)

Cinv = np.linalg.inv(C)
result = np.matmul(Cinv, D)
print("result : ", result)

