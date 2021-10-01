'''
LU Decomposition
(Doolittle's algorithm)
'''
import numpy as np

C = np.array([[5., 3., 2., 1.],
              [6., 2., 4., 5.],
              [7., 4., 1., 3.],
              [4., 3., 5., 2.]])
D = np.array([[4.],
             [2.],
             [5.],
             [1.]])

def LUDecompostion(A):
    n, _ = A.shape
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(0, n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(0, i):
                U[i, j] -= L[i, k] * U[k, j]

        for j in range(i+1, n):
            L[j, i] = A[j, i]
            for k in range(0, i):
                L[j, i] -= L[j, k] * U[k, i]

            L[j, i] /= U[i, i]

    return L, U


def SysOfLinearEquByLU(A, b):
    L, U = LUDecompostion(A)
    Y = np.matmul(np.linalg.inv(L), b)
    X = np.matmul(np.linalg.inv(U), Y)

    return X


Cinv = np.linalg.inv(C)
result = np.matmul(Cinv, D)
print("result : ", result)

resultByLU = SysOfLinearEquByLU(C, D)
print(resultByLU)



