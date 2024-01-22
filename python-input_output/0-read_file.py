#!/usr/bin/python3
"""
Module for reading and printing the content of a text file.

This module defines a function read_file that reads the content
of a specified text file (UTF8) and prints it to stdout.

Functions:
    read_file(filename=""): Read and print the content of a text file.

Usage:
    Example usage is provided at the bottom of the script.

"""


def read_file(filename=""):
    """
    Read and print the content of a text file (UTF8).

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content)


# # Example usage:
# if __name__ == "__main__":
#     read_file("my_file_0.txt")
