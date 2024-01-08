#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return multiplied_dict

# # Example Usage:
# my_dict = {'a': 3, 'b': 5, 'c': 7}
# result_dict = multiply_by_2(my_dict)

# print(result_dict)
