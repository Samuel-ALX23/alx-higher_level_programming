#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix or not matrix[0]:
        return []

    # Check if all rows have the same length
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("Matrix rows must have the same length")

    # Check if all elements are numeric
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("Matrix elements must be numeric")

    # Create a new matrix to store the squared values
    squared_matrix = []

    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element * element)
        squared_matrix.append(squared_row)

    return squared_matrix
