#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides matrix elements by a number, handling errors.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by.

    Returns:
        A new matrix with each element divided, rounded to 2 decimals.

    Raises:
        TypeError: If matrix or div invalid.
        ZeroDivisionError: If div is 0.
    """

    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be list of lists.")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Matrix rows must have equal size.")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("Matrix must be integers/floats.")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("Div must be a number.")
    if div == 0:
        raise ZeroDivisionError("Division by zero.")

    # Perform division and round
    return [[round(el / div, 2) for el in row] for row in matrix]
