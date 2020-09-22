#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            elemento = float(my_list_1[i]) / float(my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            elemento = 0
        except IndexError:
            print("out of range")
            elemento = 0
        except TypeError:
            print("wrong type")
            elemento = 0
        except ValueError:
            print("wrong type")
            elemento = 0
        finally:
            new_list.append(elemento)
    return new_list
