#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix == []:
        print()
    else:
        for i, row in enumerate(matrix):
            toAdd = []
            for j, col in enumerate(row):
                toAdd.append(matrix[i][j] * matrix[i][j])
            new_matrix.append(toAdd)
        return new_matrix
