#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result before the try block
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by 0")
    except (TypeError, ValueError):
        print("wrong type")
    finally:
        try:
            print("Inside result: {}".format(result))
        except UnboundLocalError:
            print("Inside result: None")
        return result

