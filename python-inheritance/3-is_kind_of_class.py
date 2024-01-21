#!/usr/bin/python3
"""
Module for checking if an object is an instance of,
or if it is an instance of a class
that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of
        the specified class or its subclass; otherwise False.
    """

    return isinstance(obj, a_class)

# # Example usage:
# a = 1
# if is_kind_of_class(a, int):
#     print("{} comes from {}".format(a, int.__name__))
# if is_kind_of_class(a, float):
#     print("{} comes from {}".format(a, float.__name__))
# if is_kind_of_class(a, object):
#     print("{} comes from {}".format(a, object.__name__))
