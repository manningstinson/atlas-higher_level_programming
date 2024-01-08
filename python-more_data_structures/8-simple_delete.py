#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

# # Example Usage:
# my_dict = {'banana': 3, 'apple': 5, 'orange': 2, 'grape': 7}
# simple_delete(my_dict, 'apple')
# simple_delete(my_dict, 'kiwi')  # Does nothing since 'kiwi' is not in the dictionary

# print(my_dict)
