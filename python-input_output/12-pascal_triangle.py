#!/usr/bin/python3
"""
Module: 12-pascal_triangle

Description:
This module contains a function to
generate Pascal's triangle up to a specified number of rows.

Functions:
- def pascal_triangle(n): Generates
Pascal's triangle up to n rows.

Example:
pascal_triangle(5) returns a list representing
the Pascal's triangle with 5 rows.

"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
    - n (int): The number of rows for Pascal's triangle.

    Returns:
    - list of lists: Pascal's triangle represented
    as a list of lists of integers.

    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
