#!/usr/bin/python3
"""
Module for adding items to a list and saving it to a JSON file.
"""

import sys
import json
from os import path


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: Python object to be saved.
        filename: Name of the file to save the object to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename: Name of the file to load the object from.

    Returns:
        The Python object loaded from the file.
    """
    if path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []


if __name__ == "__main__":
    # Check if add_item.json file exists, if not, create an empty list
    filename = "add_item.json"
    if not path.exists(filename):
        save_to_json_file([], filename)

    # Load existing list from file
    my_list = load_from_json_file(filename)

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)
