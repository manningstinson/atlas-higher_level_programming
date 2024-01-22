#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a text file.

Usage Example:
    nb_characters_added = append_write("file_append.txt",
     "This School is so cool!\n")
    print(nb_characters_added)
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
