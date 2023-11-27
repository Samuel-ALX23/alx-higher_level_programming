#!/usr/bin/python3
"""
This module defines a function for printing a square with the character '#'.
"""


def print_square(square_size):
    """Prints a square using the character '#'.

    Args:
        square_size: The size of the square to be printed.

    Returns:
        None

    Raises:
        TypeError: If square_size is not an integer.
        ValueError: If square_size is less than 0.
    """

    if not isinstance(square_size, int):
        raise TypeError("square_size must be an integer")
    if square_size < 0:
        raise ValueError("square_size must be >= 0")

    for i in range(square_size):
        print("#" * square_size)
