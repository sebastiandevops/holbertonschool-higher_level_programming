#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except ZeroDivisionError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except IndexError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return None
