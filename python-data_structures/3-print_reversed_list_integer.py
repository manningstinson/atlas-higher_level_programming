#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    # Check if the input list is None
    if my_list is None:
        print("Input list is None.")
        return

    for num in reversed(my_list):
        print("{:d}".format(num))
