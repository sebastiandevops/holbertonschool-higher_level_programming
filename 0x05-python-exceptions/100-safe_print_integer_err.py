#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if int(value) == value:
            print("{:d}".format(value))
            return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format\
code 'd' for object of type 'str'\n")
