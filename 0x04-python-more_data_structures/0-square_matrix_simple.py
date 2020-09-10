#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix == []:
        print()
    else:
        for i, row in enumerate(matrix):
            l = []
            for j, col in enumerate(row):
                l.append(matrix[i][j] * matrix[i][j])
            new_matrix.append(l)
        return new_matrix
