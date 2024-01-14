#!/usr/bin/python3
"""
Module for printing a text with 2 new lines after each of '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char
        if char in separators:
            lines.append(line.strip())
            lines.append("\n")
            line = ""

    if line:
        lines.append(line.strip())

    print("\n".join(lines))
