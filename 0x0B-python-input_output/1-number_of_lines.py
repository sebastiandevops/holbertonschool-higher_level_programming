#!/usr/bin/python3
"""function that returns the number of lines of a text file.
"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file.

    Args:
        filename: the file to read.

    """
    with open(filename, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
        f.close()
    return line_count
