#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    counter1 = 0
    try:
        count = 0
        for i in my_list:
            count += 1
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print()
        return counter
    except IndexError:
        print()
        return counter
