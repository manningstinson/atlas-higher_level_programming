#!/usr/bin/python3

import sys


def p():
    n = len(sys.argv) - 1
    if n == 0:
        print("No arguments.")
    else:
        s = 's' if n > 1 else ''
        print("Number of arg{}: {}{}".format(s, n, '' if n == 1 else 's'))
        for i, a in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, a))


if __name__ == "__main__":
    p()
