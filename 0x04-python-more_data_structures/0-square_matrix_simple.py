#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    if new_matrix == [[]]:
        print()
    else:
        for i, row in enumerate(new_matrix):
            for j, col in enumerate(row):
                new_matrix[i][j] = new_matrix[i][j] * new_matrix[i][j]
        return new_matrix
