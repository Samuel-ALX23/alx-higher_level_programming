#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None or not isinstance(my_string, str):
        return None

    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
