#!/usr/bin/python3

"""
This module provides a function to read the content of a text file
Print it to stdout.
The function read_file accepts a filename as a parameter
Reads the content of the file using WITH statement
WITH statement ensure proper file handling.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    :param filename: The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    # Example usage:
    # read_file("my_file_0.txt")
    pass