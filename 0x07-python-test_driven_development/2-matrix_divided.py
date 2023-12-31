#!/usr/bin/python3

"""Define a Matrix class"""


def matrix_divided(matrix, div):
    """A matrix class"""
    # Check if matrix is a list of lists of integers or floats
    if (not all(
        isinstance(row, list) and all(
            isinstance(num, (int, float)) for num in row)
        for row in matrix)):
        raise TypeError("matrix must be a matrix of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return (new_matrix)
