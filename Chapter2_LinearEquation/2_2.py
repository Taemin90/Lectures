'''
Unique Solution
Gauss-Jordan elimination method
'''

import numpy as np

def gauss(A):
    row, col = A.shape

    pivot = 0
    for i in range(0, row):
        if A[i][i] == 0:
            for j in range(i+1, row):
                if A[j][i] != 0:
                    temp = A[j]
                    A[j] = A[i]
                    A[i] = temp
                    break

        A[i] = A[i] / A[i][i]

        for j in range(0, row):
            if i != j:
                A[j] -= A[i] * A[j][i]

    result = []
    for i in range(0, row):
        result.append(A[i][col-1])

    return result


A = np.array([[2., 2., 4., 18.],
              [1., 3., 2., 13.],
              [3., 1., 3., 14.]])

result = gauss(A)
print(result)

