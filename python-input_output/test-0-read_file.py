import doctest
import '0-read_file' as read_file  # Import with single quotes


# Doctests for the 0-read_file module
"""
This module provides a function to read the content of a text file (UTF8) and print it to stdout.

>>> import 0-read_file  # Import the module to test

>>> 0-read_file.read_file("my_file_0.txt")
This is the content of my_file_0.txt

>>> 0-read_file.read_file("nonexistent_file.txt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "0-read_file.py", line 11, in read_file
    with open(filename, 'r', encoding='utf-8') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
"""

# Run the doctests
doctest.testmod(0-read_file)
