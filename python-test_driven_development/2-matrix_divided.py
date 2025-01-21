#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                'Each row of the matrix must have the same size'
            )
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
    return [[round(elem / div, 2) for elem in row] for row in matrix]
