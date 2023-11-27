#!/usr/bin/python3
"""
Module to find the maximum integer in a list.
"""


def find_max_integer(integer_list=[]):
    """Finds and returns the maximum integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(integer_list) == 0:
        return None

    max_value = integer_list[0]
    i = 1
    while i < len(integer_list):
        if integer_list[i] > max_value:
            max_value = integer_list[i]
        i += 1

    return (max_value)
