#!/usr/bin/python3
"""
This module defines a function for adding two numbers.
"""


def add_numbers(num1, num2=98):
    """Addition of two integer or float numbers.

    Args:
        num1: The first number.
        num2: The second number. Default value is 98.

    Returns:
        The sum of the two numbers.

    Raises:
        TypeError: If num1 or num2 are not integer or float numbers.
    """

    if not (isinstance(num1, int) or isinstance(num1, float)):
        raise TypeError("num1 must be an integer or float")
    if not isinstance(num2, int) and not isinstance(num2, float):
        raise TypeError("num2 must be an integer or float")

    return int(num1) + int(num2)
