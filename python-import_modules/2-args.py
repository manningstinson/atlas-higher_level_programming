#!/usr/bin/python3

import sys


def print_arguments():

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("No arguments.")
    else:
        plural_s = 's' if num_args > 1 else ''
        print(f"Number of argument{plural_s}: {num_args}"
              f"{'' if num_args == 1 else 's'}")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()
