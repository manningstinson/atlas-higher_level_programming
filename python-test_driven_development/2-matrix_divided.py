#!/usr/bin/python3
"""Divide a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given number.

    Args:
    - matrix (list of lists): Matrix of integers or floats.
    - div (int or float): Number to divide each element of the matrix.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats,
      if each row of the matrix does not have the same size,
      or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.

    Returns:
    - list of lists: New matrix with elements rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    result_matrix = matrix_divided(matrix, 3)
    print(result_matrix)
