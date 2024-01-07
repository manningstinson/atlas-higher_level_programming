#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    elements_printed = 0
    for i in range(x):
        try:
            # Print elements without spaces
            print(my_list[i], end='')  
            elements_printed += 1
        except IndexError:
            # Exit the loop when an IndexError occurs
            break  
    # Print a newline after all elements
    print()  
    return elements_printed
