#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix.
        div (int or float): The number to divide by.

    Returns:
        list of lists: The new matrix.

    Raises:
        TypeError: If matrix is not a list of lists or if the elements of the
        lists are not integers or floats or if div is not an integer or float.
        ZeroDivisionError: If div is 0.
        ValueError: If the rows of the matrix are not the same size.
    """
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(row is not None and len(row) > 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(None not in row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if div is None:
        raise TypeError("div must be a number")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
