#!/usr/bin/python3

def safe_print_integer(value):

    try:
        # Attempt to format as integer and print
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        # Handle errors if value cannot be converted to integervi
        return False
