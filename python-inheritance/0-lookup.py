#!/usr/bin/python3

"""
Module: object_inspector

This module provides a function to inspect an object
and return a list of its available attributes and methods.

Functions:
- lookup(obj): Returns a list containing the names
of attributes and methods of the object.

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

    # Remove the filtering condition to include all attributes and methods
    return all_attributes

# # Example usage
# if __name__ == "__main__":
#     example_object = 42  # Replace with the object you want to inspect
#     result = lookup(example_object)
#     print(result)
