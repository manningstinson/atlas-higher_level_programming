#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Attempt to divide elements
            element_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            element_result = 0
        except (TypeError, ValueError):
            # Handle wrong type
            print("wrong type")
            element_result = 0
        except IndexError:
            # Handle out of range
            print("out of range")
            element_result = 0
        finally:
            # Add the result to the result_list
            result_list.append(element_result)

    return result_list
