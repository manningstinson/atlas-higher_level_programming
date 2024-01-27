#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    # Skip the script name (argv[0]) and convert the rest to integers
    numbers = [int(arg) for arg in argv[1:]]

    result = sum(numbers)

    print(result)
