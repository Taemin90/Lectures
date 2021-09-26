'''
matmul() : matrix multiplication
linalg.matrix_power() : matrix to the power of n
block() : make a block matrix
diag() : make a diagonal matrix
'''

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[2, 2],
              [1, 3]])
C = np.array([[4, 5, 6],
              [7, 8, 9]])
v = np.array([[10],
              [20]])
D11 = np.array([[1, 2],
                [3, 4]])
D12 = np.array([[5],
                [6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])

print("A+B : ", A+B)
print("A-B : ", A-B)
print("3A : ", 3*A)
print("2v : ", 2*v)
print("AB(np.matmul(A, B)) : ", np.matmul(A, B))
print("AC(np.matmul(A, C)) : ", np.matmul(A, C))
print("Av(np.matmul(A, v)) : ", np.matmul(A, v))
print("A^2(np.linalg.matrix_power(A, 2)) : ", np.linalg.matrix_power(A, 2))
print("A^3(np.linalg.matrix_power(A, 3)) : ", np.linalg.matrix_power(A, 3))
print("A*B : ", A*B)
print("A/B : ", A/B)
print("A**2 : ", A**2)
print("A.T : ", A.T)
print("v.T : ", v.T)

diagM = np.diag([1, 2, 3])
print("diagonal matrix : ", diagM)

D = np.block([[D11, D12],
             [D21, D22]])

print("D : ", D)

