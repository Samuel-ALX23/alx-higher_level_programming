#!/usr/bin/python3
def __init__(self, size=0):
    """Initializes a new square.

    Args:
        size (int): The size of the new square.
    """
    self.__size = size

    if not isinstance(size, int):
        raise TypeError("Size must be an integer.")
    elif size < 0:
        raise ValueError("Size must be >= 0.")
    else:
        self.__size = int(size)
