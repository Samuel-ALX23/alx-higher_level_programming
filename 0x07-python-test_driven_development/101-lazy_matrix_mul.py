#!/usr/bin/python3.5
"""
This module defines a function for matrix multiplication.
It uses the numpy library for efficient matrix operations.
"""


import numpy as np


def matrix_multiplication(matrix_a, matrix_b):
    """Multiplies two matrices.

    Args:
        matrix_a: The first matrix.
        matrix_b: The second matrix.

    Returns:
        The result of the matrix multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """

    result = np.matmul(matrix_a, matrix_b)
    return (result)
