#!/usr/bin/python3
"""
Module for reading a text file and printing it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the text file.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
