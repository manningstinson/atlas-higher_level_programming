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
    try:
        with open(filename, encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Test Case: Correct output - case: 1 line
    read_file("my_file_0.txt")

    # Test Case: Correct output - case: not found
    read_file("nonexistent_file.txt")

    # Test Case: Correct output - case: empty
    read_file("empty_file.txt")

    # Test Case: Correct output - case: big HTML text
    read_file("big_html_file.txt")

    # Test Case: Correct output - case: 5 paragraphs
    read_file("five_paragraphs.txt")
