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
    result = [[sum(a * b for a, b in zip(m_a_row, m_b_col))
              for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return result
