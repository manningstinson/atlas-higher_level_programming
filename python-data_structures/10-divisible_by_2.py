#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    # Create a new list to store True or False values
    result_list = [num % 2 == 0 for num in my_list]

    return result_list
