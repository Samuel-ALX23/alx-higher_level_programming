#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list is None:
        return None
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
