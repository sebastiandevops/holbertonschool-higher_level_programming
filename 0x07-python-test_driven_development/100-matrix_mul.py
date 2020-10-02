#!/usr/bin/python3
"""function that multiplies 2 matrices.
m_a and m_b must be an list of lists of integers or floats,
if m_a or m_b is not a list: raise a TypeError exception
with the message m_a must be a list or m_b must be a list.
if m_a or m_b is not a list of lists: raise a TypeError
exception with the message m_a must be a list of lists
or m_b must be a list of lists.
if m_a or m_b is empty (it means: = [] or = [[]]):
raise a ValueError exception with the message
m_a can't be empty or m_b can't be empty.
if one element of those list of lists is not an integer or
a float: raise a TypeError exception with the message m_a
should contain only integers or floats or m_b should
contain only integers or floats.
if m_a or m_b is not a rectangle (all ‘rows’ should be
of the same size): raise a TypeError exception with the
message each row of m_a must be of the same size or each
row of m_b must be of the same size.
If m_a and m_b can’t be multiplied: raise a ValueError
exception with the message m_a and m_b can't be multiplied
"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices.

    Args:
        m_a (list): matrix to be multiplied.
        m_b (list): matrix to multiply.
    Returns:
        Multiplied matrix printed.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for l in m_a:
        if type(l) != list:
            raise TypeError("m_a must be a list of lists")
    for l in m_b:
        if type(l) != list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for l in m_a:
        for number in l:
            if isinstance(number, (int, float)) is False:
                raise TypeError("m_a should contain only integers or floats")
    for l in m_b:
        for number in l:
            if isinstance(number, (int, float)) is False:
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    for l in m_a:
        if type(l) == list:
            if len(l) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")
    else:
        result = [[sum(a * b for a, b in zip(m_a_row, m_b_col))
                   for m_b_col in zip(*m_b)] for m_a_row in m_a]
        return result
