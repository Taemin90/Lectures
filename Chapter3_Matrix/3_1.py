'''
vstack function : make a matrix which has given vectors as rows
column_vstack function : make a matrix which has given vectors as columns
'''

import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

A = np.vstack([v1, v2, v3])
print("A : ", A)

B = np.column_stack([v1, v2, v3])
print("B : ", B)

C = np.array([[1, 2],
             [3, 4],
             [5, 6]])

D = np.column_stack([C, v3])
print("D : ", D)

E = np.array([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]])

print("1row, 4column : ", E[0, 3])
print("2row, 3column : ", E[1, 2])
print("1~2row, 3column : ", E[0:2, 2])
print("1~2row, 3~4column : ", E[0:2, 2:4])
print("3row : ", E[2, ])

E[0, 0] = -1
print("E : ", E)