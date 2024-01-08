#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary before deleting
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# # Example Usage:
# a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
# new_dict = simple_delete(a_dictionary, 'a')

# # Printing the sorted original dictionary
# for key, value in sorted(a_dictionary.items()):
#     print(f"{key}: {value}")

# print("--")

# # Printing the sorted dictionary after deletion
# for key, value in sorted(new_dict.items()):
#     print(f"{key}: {value}")
