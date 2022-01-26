import numpy as np

import math
import A

K = input()
Matrix_M = [[A.row_A[A.col_A[0].index(p)][k] for k in range(0, K + 1)] for p in A.col_A[0]]

a = list()
N = []
V = []
for i in A.col_A[0][range(1, len(A.col_A[0] + 1))]:
    for P in A.Col_A[0]:
        a.append(A.row_A[[A.row_A[A.col_A[0].index(i)]]][[A.row_A[A.col_A[0].index(p)]]])
        N.append(max(a))
        if N[i] < 0.5:
            b = np.std(A.row_A[i + 1][1:]) / 2 * (math.sqrt(K)) * (np.mean(A.row_A[i][1:]))
            V.append(b)
        else:
            b = np.std(A.row_A[i + 1][1:]) / (np.mean(A.row_A[i][1:]))
            V.append(b)

Co = sum(N)
Me = sum(V)
Weight = Co + Me
print(Weight)
