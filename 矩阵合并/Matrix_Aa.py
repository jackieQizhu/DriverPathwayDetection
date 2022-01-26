import pandas as pd
import numpy as np
import csv

'''
matrixS = pd.DataFrame(pd.read_csv("E:\\Data analysis\\install\\S.csv"))
matrixC = pd.DataFrame(pd.read_csv("E:\\Data analysis\\install\\C.csv"))

print(matrixC, '\n', matrixS)
'''
# Row_a replace Matrix A1
#  def Row_a(): 定义矩阵A1的行
with open('E:\\Data analysis\\install\\S.csv', 'r', encoding='utf-8') as S:
    row_s = list(csv.reader(S))  # 转为列表，遍历矩阵行
    print(row_s[0], end='\n')  # 筛选行
    col_s = list(np.transpose(list(csv.reader(S))))  # 转为列表，遍历矩阵列
    print(col_s[0], end='\n')  # 遍历矩阵的列
with open('E:\\Data analysis\\install\\C.csv', 'r', encoding='utf-8') as C:
    row_c = list(csv.reader(C))
    print(row_c[0], end='\n')
    col_c = list(np.transpose(list(csv.reader(S))))
    print(col_c[0], end='\n')
row_a = list(set(row_s[0]).union(set(row_c[0])))  # 新矩阵的第一行 基因

''' def Col_a():   定义矩阵A1的列
#with open('E:\\Data analysis\\install\\S.csv', 'r', encoding='utf-8') as S:
# with open('E:\\Data analysis\\install\\C.csv', 'r', encoding='utf-8') as S:
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
np.savetxt('E:\\Data analysis\\install\\Matrix_a.csv', Matrix_a, delimiter=',')
