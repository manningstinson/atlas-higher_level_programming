#!/usr/bin/python3


def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize a variable to store the biggest integer
    biggest_integer = my_list[0]  # Start with the first element

    # Loop through the list, starting from the second element
    for num in my_list[1:]:  # Iterate from the second element onwards
        if num > biggest_integer:
            biggest_integer = num

            # Return the biggest integer
            return biggest_integer
