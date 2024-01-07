#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by 0")
        return None
    except (TypeError, ValueError):
        print("wrong type")
        return None
    finally:
        print("Inside result: {}".format(result))

    return result
