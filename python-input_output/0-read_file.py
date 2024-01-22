#!/usr/bin/python3
"""Module for reading and printing the contents of a text file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    read_file("my_file_0.txt")
