#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    # Check if the input list is None
    if my_list is None:
        print("Input list is None.", end='')  # Use end='' to avoid adding an extra newline
        return

    # Iterate through the reversed list and print each integer using str.format()
    for num in reversed(my_list):
        print("{:d}".format(num))
