import pandas as pd
import numpy as np
import csv
import Matrix_Aa

'''matrixS = pd.DataFrame(pd.read_csv("E:\\Data analysis\\install\\1.csv"))
matrixC = pd.DataFrame(pd.read_csv("E:\\Data analysis\\install\\2.csv"))

print(matrixC, '\n', matrixS)
'''

# def Row_A():
with open('E:\\Data analysis\\install\\Matrix_a.csv', 'r', encoding='utf-8') as A:
    row_A = list(csv.reader(A))  # 转为列表，遍历矩阵行
    print(row_A[0], end='\n')  # 筛选行c

with open('E:\\Data analysis\\install\\??.csv', 'r', encoding='utf-8') as D:
    row_D = list(csv.reader(D))
    print(row_D[0], end='\n')
row_G = list(set(row_A[0]).union(set(row_D[0])))  # 新矩阵的第一行 基因



# def Col_A():
with open('E:\\Data analysis\\install\\1.csv', 'r', encoding='utf-8') as Aa:
    col_A = list(np.transpose(list(csv.reader(Aa))))  # 转为列表，遍历矩阵列
    print(col_A[0], end='\n')  # 遍历矩阵的列

with open('E:\\Data analysis\\install\\2.csv', 'r', encoding='utf-8') as Dd:
    col_D = list(np.transpose(list(csv.reader(Dd))))
    print(col_D[0], end='\n')



# def matrix_A():  # 构造矩阵
col = [[0 for i in range(len(row_G[0]))] for j in range(len(col_A[0]))]
for i in row_G:  # 遍历基因并集行
    if i in row_A[0]:  # 若基因i在矩阵S中
        s = row_A[0].index(i)  # 返回为i在列表中的位置
        for j1 in range(1, len(col_A[s]) + 1):  # j1为遍历i位置下列的每个元素，置1或置0
            try:
                if col_A[j1][s] == 1 and col_D[j1][s] != 0:
                    col_A[j1][s] = 1
            except:
                if col_A[j1][s] == 1:
                    col[j1][s] = 1
        print(col_A)
        print(col_A[row_A[0].index(i)])
    else:  # 否则在矩阵C中
        print(col_D[row_D[0].index(i)])
    global col
Matrix_A = [[col[i][j] for i in range(len(row_G[0]))] for j in range(len(col_A[0]))]  # 定义二维矩阵


np.savetxt('Matrix_A', Matrix_A , delimiter=',')
