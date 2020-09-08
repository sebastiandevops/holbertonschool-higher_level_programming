#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        return tuple_b
    elif tuple_b == ():
        return tuple_a
    elif len(tuple_a) < 2:
        new_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    elif len(tuple_b) < 2:
        new_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    else:
        new_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return new_tuple
