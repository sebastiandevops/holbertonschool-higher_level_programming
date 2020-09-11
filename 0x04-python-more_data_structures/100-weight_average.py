#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        result = 0
        prom = 0
        for i, j in my_list:
            result += i * j
            prom += j
        result = result / prom
        return result
