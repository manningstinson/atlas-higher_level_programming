#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

# # Example Usage:
# my_dict = {'banana': 3, 'apple': 5, 'orange': 2, 'grape': 7}
# print_sorted_dictionary(my_dict)
