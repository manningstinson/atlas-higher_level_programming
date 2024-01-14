#!/usr/bin/python3
"""
This module provides a function for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float.
            Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If a or b is NaN.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float) and (a % 1 != 0 or a != a):
        raise ValueError("a must be an integer or b must be an integer")

    if isinstance(b, float) and (b % 1 != 0 or b != b):
        raise ValueError("a must be an integer or b must be an integer")

    return int(a + b)

