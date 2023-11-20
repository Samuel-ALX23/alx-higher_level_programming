#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if not my_list or x < 0:
        return 0

    if x > len(my_list):
        x = len(my_list)

    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except Exception as e:
            break

    print()
    return (count)
