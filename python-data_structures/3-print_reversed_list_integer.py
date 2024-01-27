#!/usr/bin/python3


def print_reversed_list_integer(my_list=None):
    # Check if the input list is None
    if my_list is None:
        return

    for num in reversed(my_list):
        print("{:d}".format(num))


if __name__ == "__main__":
    print_reversed_list_integer()
