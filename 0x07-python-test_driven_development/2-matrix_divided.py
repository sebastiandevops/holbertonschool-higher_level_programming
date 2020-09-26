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
