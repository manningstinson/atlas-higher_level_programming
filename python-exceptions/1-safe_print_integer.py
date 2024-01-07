#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Only print if conversion to integer is successful
        if isinstance(int(value), int):
            print("{:d}".format(int(value)))
            return True
        else:
            return False
        except (ValueError, TypeError):
            # Handle errors if value cannot be converted to integer
            return False
