#!/usr/bin/python3
"""Function that reads n lines of a text file (UTF8)
and prints it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file (UTF8)
and prints it to stdout.

    Args:
        filename: the file to read.
        nb_lines (int): number of lines to read,

    """
    with open(filename, 'r') as f:
        all_lines = f.readlines()
        lines = all_lines[:nb_lines]
        stri = " "
        stri = stri.join(lines)
        if nb_lines <= 0 or nb_lines >= len(all_lines):
            print(stri.join(all_lines).lstrip(), end='')
        else:
            print(stri.lstrip(), end='')
