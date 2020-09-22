#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value and not isinstance(value, bool):
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
    except TypeError:
        return False
