#!/usr/bin/python3


def max_integer(my_list=[]):

    # Check if the list is empty
    if not my_list:
        return None

    # Initialize a variable to store the biggest integer
    biggest_integer = my_list[0]

    # Loop through the list and compare each element to the current biggest
    for num in my_list:
        if num > biggest_integer:
            biggest_integer = num

            # Return the biggest integer
            return biggest_integer
