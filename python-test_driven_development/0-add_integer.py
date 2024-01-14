#!/usr/bin/env python3

"""
This module provides a function for adding two integers.

Functions:
    add_integer(a, b=98): Adds two integers.

Usage:
    result = add_integer(5, 3)
    print(result)  # Output: 8
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
        ValueError: If a or b is a string, or if result is NaN.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float) and (a.is_integer() or a.is_nan()):
        a = int(a)

    if isinstance(b, float) and (b.is_integer() or b.is_nan()):
        b = int(b)

    result = a + b

    if isinstance(result, float) and result.is_integer():
        return int(result)

    raise ValueError("Result is NaN or not a valid integer.")

# if __name__ == "__main__":
#     # Example usage
#     result = add_integer(5, 3)
#     print(result)  # Output: 8
