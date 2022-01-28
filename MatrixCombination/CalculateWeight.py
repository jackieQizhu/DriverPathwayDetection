# above is my original code
# i will rewrite them
import random
import copy
import numpy as np

import pandas as pd

matrix_A = pd.DataFrame(pd.read_csv("./tcga_data/AA.csv",
                                    header=0, index_col=0))
K = int(input())

'''
# a submatrix of matrix_A which is determined by K
m_gene_set = random.sample(matrix_A.columns, K)
m_patient_set = set(matrix_A.index)


matrix_M = pd.DataFrame((["{0}#{1}".format(row, col) for col in m_gene_set] for row in m_patient_set),
                        index=m_patient_set, columns=m_gene_set)
'''

# A more convenient way
sqrt = np.sqrt(K)
matrix_M = matrix_A.iloc[:, 0:K]
Eta = []
Upsilon = []
Sigma = []
Mu = []
i = 0
# index属性遍历
for index in matrix_M.index:
    maximum = max(matrix_M.loc[index])
    standard = matrix_M.loc[index].std()
    average = matrix_M.loc[index].mean()
    Eta.append(maximum)
    Sigma.append(standard)
    Mu.append(average)

for i in range(len(Eta)):
    if Eta[i] < 0.5:
        value = Sigma[i] / (2 * sqrt * Mu[i])
        Upsilon.append(value)
    else:
        value = Sigma[i] / Mu[i]
        Upsilon.append(value)

Coverage = sum(Eta)
Mutual_exclusivity = sum(Upsilon)
Weight = Coverage + Mutual_exclusivity
print(Weight)  # 15.678234025867871
