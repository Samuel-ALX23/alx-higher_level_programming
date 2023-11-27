#!/usr/bin/python3
"""
This module defines a function for dividing the numbers of a matrix.
"""


def divide_matrix(matrix, divisor):
    """Divides the integer or float numbers in a matrix.

    Args:
        matrix: A list of lists containing integer or float numbers.
        divisor: The number by which the matrix elements will be divided.

    Returns:
        A new matrix with the results of the division.

    Raises:
        TypeError:
            If the elements of the matrix are not lists.
            If the elements of the lists are not integers or floats.
            If the divisor is not an integer or float number.
            If the lists of the matrix do not have the same size.

        ZeroDivisionError: If the divisor is zero.
    """

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    type_error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(type_error_msg)

    len_e = 0
    size_error_msg = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(type_error_msg)

        if len_e != 0 and len(elements) != len_e:
            raise TypeError(size_error_msg)

        for num in elements:
            if not isinstance(num, (int, float)):
                raise TypeError(type_error_msg)

        len_e = len(elements)

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / divisor, 2), x)), matrix))

    return (new_matrix)
