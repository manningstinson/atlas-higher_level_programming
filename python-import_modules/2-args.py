#!/usr/bin/python3

import sys

def print_command_line_args():
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("No arguments.")
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))

    if num_args >= 1:
        position = 0
        for argument in sys.argv:
            if position != 0:
                print("{}: {}".format(position, argument))
            position += 1

if __name__ == "__main__":
    print_command_line_args()
