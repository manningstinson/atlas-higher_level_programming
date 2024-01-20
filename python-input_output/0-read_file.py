#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    :param filename: The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

# Example usage:
# read_file("my_file_0.txt")
