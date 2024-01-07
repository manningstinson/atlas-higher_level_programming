#!/usr/bin/python3

def safe_print_division(a, b):

    result = None  # Initialize result before the try block
    try:
        result = a / b
        print(f"{a} / {b} = {result}")  # Print the result only if division is successful
    except ZeroDivisionError:
        print("division by 0")
    except (TypeError, ValueError):
        print("wrong type")
    finally:
        print(f"Inside result: {result}")  # Always print the result, even if an error occurred
        return result

