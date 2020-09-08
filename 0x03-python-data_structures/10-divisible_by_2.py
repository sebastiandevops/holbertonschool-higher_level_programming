#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for num in new_list:
        if num % 2 == 0:
            new_list[num] = True
        else:
            new_list[num] = False
    return new_list
