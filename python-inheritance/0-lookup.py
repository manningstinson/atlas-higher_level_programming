#!/usr/bin/python3

"""
Module: object_inspector

This module provides a function to inspect an object
and return a list of its available attributes and methods.

Functions:
- lookup(obj): Returns a list
containing the names of attributes and methods of the object.

Usage:
Example usage is demonstrated at the end of the file.

Note:
This module does not import any external modules.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: The object to inspect.

    Returns:
    - A list containing the names of attributes and methods of the object.
    """
    # Get all attributes and methods of the object
    all_attributes = dir(obj)

    # Filter attributes and methods starting with '__'
    filtered_attributes = [a for a in all_attributes if a.startswith('__')]

    return filtered_attributes


# Test cases


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
