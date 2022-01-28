import pandas as pd
import copy
import numpy as np
import csv

matrix_a = pd.DataFrame(pd.read_csv("./tcga_data/a.csv",
                                    header=0, index_col=0))
matrix_d = pd.DataFrame(pd.read_csv("./tcga_data/D.csv",
                                    header=0, index_col=0))

# omissible definition -matrix_d_filter-
matrix_d_filter = copy.deepcopy(matrix_d)
matrix_d_filter[(matrix_d_filter.abs() != 0)] = 1

lambda_1 = 3
lambda_2 = 7

d_gene_set, d_patient_set = set(matrix_d_filter.columns), set(matrix_d_filter.index)
a_gene_set, a_patient_set = set(matrix_a.columns), set(matrix_a.index)

gene_union_set = set(d_gene_set | a_gene_set)
patient_union_set = set(d_patient_set | a_patient_set)
gene_intersection_set = set(a_gene_set & d_gene_set)
patient_intersection_set = set(a_patient_set & d_patient_set)

matrix_A = pd.DataFrame((["{0}#{1}".format(row, col) for col in gene_union_set] for row in patient_union_set),
                        index=patient_union_set, columns=gene_union_set)


def union_matrix(x):
    gene, patient = tuple(x.split("#"))
    if patient in patient_intersection_set and gene in gene_intersection_set:
        if matrix_a.loc(patient, gene) == 1 and lambda_2 > matrix_d.loc(patient, gene) >= lambda_1:
            return 1.5
        if matrix_a.loc(patient, gene) == 0 and matrix_d.loc(patient, gene) >= lambda_2:
            max_d = max(matrix_d.loc[:, gene])
            normalization_process = 2 * max_d
            return matrix_d.loc(patient, gene)/normalization_process
    else:
        return 0




print("prev: \n", matrix_A)
union_df = matrix_A.applymap(union_matrix)
print("after: \n", union_df)

exit(0)
