#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int/float): Number to divide the elements.

    Returns:
        list: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists, div is not a number,
                   or rows in matrix are not of the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
