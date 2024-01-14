#!/usr/bin/python3
"""
This module provides a function for adding two integers.

Functions:
    add_integer(a, b=98): Adds two integers.

Usage:
    result = add_integer(5, 3)
    print(result)  # Output: 8
"""

import math

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
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float) and (a.is_integer() or math.isnan(a)):
        a = int(a)

    if isinstance(b, float) and (b.is_integer() or math.isnan(b)):
        b = int(b)

    return int(a + b)
