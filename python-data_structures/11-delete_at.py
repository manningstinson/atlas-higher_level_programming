#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return

    # Remove the item by slicing and reassigning to the same list
    del my_list[idx]  # This line modifies the original list
