#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None or not isinstance(my_list, list):
        return None

    for i in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]))
