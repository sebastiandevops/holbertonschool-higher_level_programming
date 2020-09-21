#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter1 = 0
    counter2 = 0
    try:
        print(*my_list[:x], sep='')
        for i in my_list[:x]:
            counter1 += 1
        return counter1
    except IndexError:
        for i in range(my_list[:counter1]):
            print(*my_list[:counter1], sep='')
            counter2 += 1
        return counter2
