#!/usr/bin/python3

"""
Module: object_inspector

This module provides a function to inspect an object 
Return a list of its available attributes and methods.

Functions:
- lookup(obj): Returns a list 
Containing the names of attributes and methods of the object.

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

    # Filter out attributes and methods that don't start with '__'
    filtered_attributes = [attr for attr in all_attributes if attr.startswith('__')]

    return filtered_attributes

# Example usage:
if __name__ == "__main__":
    class ExampleClass:
        def __init__(self):
            self.name = "Example"
        
        def say_hello(self):
            print("Hello!")

    example_obj = ExampleClass()

    # Get and print the list of attributes and methods of the object
    attributes_and_methods = lookup(example_obj)
    print(attributes_and_methods)
