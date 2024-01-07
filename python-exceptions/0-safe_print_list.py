#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    elements_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end='')  # Print elements without spaces
            elements_printed += 1
        except IndexError:
            break  # Exit the loop when an IndexError occurs

    print()  # Print a newline after all elements
    return elements_printed
