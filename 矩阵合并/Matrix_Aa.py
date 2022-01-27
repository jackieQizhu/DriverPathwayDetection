import pandas as pd
import numpy as np
import csv

# 1. Use the relative path instead of the absolute path
# 2. Naming the directory as "_" to connect, don't use space ' '
matrix_s = pd.DataFrame(pd.read_csv("../tcga_data/ModuleData/S.csv",
                                    header=0, index_col=0))
matrix_c = pd.DataFrame(pd.read_csv("../tcga_data/ModuleData/C.csv",
                                    header=0, index_col=0))
lambda_1 = 0.6
# def filter_matrix_c_lambda_1(num):
matrix_c_filter_lambda1 = matrix_c.copy()
matrix_c_filter_lambda1[(matrix_c.abs() >= lambda_1)] = 1

s_gene_set, s_patient_set = set(matrix_s.columns), set(matrix_s.index)
c_gene_set, c_patient_set = set(matrix_c_filter_lambda1.columns), set(matrix_c_filter_lambda1.index)

# get the union for row names and col names
gene_union_set = (s_gene_set | c_gene_set)
patient_union_set = (s_patient_set | c_patient_set)
gene_intersect_set = (s_gene_set & c_gene_set)
patient_intersect_set = (s_patient_set & c_patient_set)

union_df = pd.DataFrame((["{0}#{1}".format(row, col) for col in gene_union_set] for row in patient_union_set),
                        index=patient_union_set, columns=gene_union_set)

print(matrix_s[(matrix_s.index == "p2")]["gene1"] == 0)


def apply_track(x):
    patient, gene = tuple(x.split("#"))
    # process the intersect case
    if patient in patient_intersect_set and gene in gene_intersect_set:
        return matrix_s.loc[patient, gene] | matrix_c_filter_lambda1.loc[patient, gene]
    # process the case which the cases are in the s set
    if patient in s_patient_set and gene in s_gene_set:
        return matrix_s.loc[patient, gene]
    # process the case which the cases are in the c set
    if patient in c_patient_set and gene in c_gene_set:
        return matrix_c_filter_lambda1.loc[patient, gene]
    # If the case is neither in S set nor in C set, then just fill in 0
    else:
        return 0


print("prev: \n", union_df)
union_df = union_df.applymap(apply_track)
print("after: \n", union_df)

exit(0)

## I needs to rewrite your codes and the following is your code
## This operation can be implemented using pandas in an elegant way

# Row_a replace Matrix A1
#  def Row_a(): 定义矩阵A1的行
with open('../tcga_data/ModuleData/S.csv', 'r', encoding='utf-8') as S:
    row_s = list(csv.reader(S))  # 转为列表，遍历矩阵行
    print(row_s[0], end='\n')  # 筛选行
    col_s = list(np.transpose(list(csv.reader(S))))  # 转为列表，遍历矩阵列
    print(col_s[0], end='\n')  # 遍历矩阵的列
with open('../tcga_data/ModuleData/C.csv', 'r', encoding='utf-8') as C:
    row_c = list(csv.reader(C))
    print(row_c[0], end='\n')
    col_c = list(np.transpose(list(csv.reader(S))))
    print(col_c[0], end='\n')
row_a = list(set(row_s[0]).union(set(row_c[0])))  # 新矩阵的第一行 基因

''' def Col_a():   定义矩阵A1的列
#with open('../tcga_data/ModuleData/S.csv', 'r', encoding='utf-8') as S:
# with open('../tcga_data/ModuleData/C.csv', 'r', encoding='utf-8') as S:
    '''

# def matrix_a():  构造矩阵
col = [[0 for i in range(len(row_a[0]))] for j in range(len(col_s[0]))]
for i in row_a:  # 遍历基因并集行
    if i in row_s[0]:  # 若基因i在矩阵S中
        s = row_s[0].index(i)  # 返回为i在列表中的位置
        for j1 in range(1, len(col_s[s]) + 1):  # j1为遍历i位置下列的每个元素，置1或置0
            try:
                if (col_s[j1][s] == 1) and (col_c[j1][s] != 0):
                    col_s[j1][s] = 1
                elif col_s[j1][s] == 1:
                    col[j1][s] = 1
            finally:
                col[j1][s] = 1

        print(col_s)
        print(col_s[row_s[0].index(i)])
    else:  # 否则在矩阵C中
        print(col_c[row_c[0].index(i)])

Matrix_a = [[col[i][j] for i in range(len(row_a[0]))] for j in range(len(col_s[0]))]  # 定义二维矩阵
print(Matrix_a)
np.savetxt('../tcga_data/ModuleData/Matrix_a.csv', Matrix_a, delimiter=',')
