#!/usr/bin/python3
"""
Module that provides matrix division functionality.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list): List of lists of integers/floats
        div (int/float): Number to divide by

    Returns:
        New matrix with all elements divided by div
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check matrix type
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    # Check elements type
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg)

    # Check rows size
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
