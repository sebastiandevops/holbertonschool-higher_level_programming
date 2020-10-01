#!/usr/bin/python3
"""function that divides all elements of a matrix,
matrix must be a list of lists of integers or floats,
otherwise raise a TypeError exception,
Each row of the matrix must be of the same size,
otherwise raise a TypeError exception.
div must be a number (integer or float),
otherwise raise a TypeError exception
div can’t be equal to 0,
otherwise raise a ZeroDivisionError exception
with the message a must be an integer or b must be an integer

"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    Args:
        matrix (list): lists of integers or floats.
        div (int, float): integer or float to divide the matrix elements.

    Returns:
        Returns a new matrix.
    """
    s = "Each row of the matrix must have the same size"
    m = 'matrix must be a matrix (list of lists) of integers/floats'
    new_matrix = []
    print(len(matrix))
    if matrix == []:
        print()
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError(s)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i, row in enumerate(matrix):
            toAdd = []
            for j, col in enumerate(row):
                if isinstance(matrix[i][j], (int, float)) is False:
                    raise TypeError(m)
                else:
                    toAdd.append(round((matrix[i][j] / div), 2))
            new_matrix.append(toAdd)
    return new_matrix
