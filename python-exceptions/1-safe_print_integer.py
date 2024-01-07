#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):


    # Initialize a variable to count the elements printed
    elements_printed = 0

    # Use try-except to handle potential IndexError
    try:

        # Iterate through the list and print each element
        for i in range(x):
            print(my_list[i], end=' ')
            elements_printed += 1
    except IndexError:
        # Catch the IndexError if x is greater than the length of my_li
        pass

    # Print a newline after the elements
    print()

    return elements_printed
