#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # If the key exists, update its value; otherwise, add a new key/value pair
    a_dictionary[key] = value
    return a_dictionary

# # Example Usage:
# a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
# new_dict = update_dictionary(a_dictionary, 'language', "Python")

# # Printing the sorted dictionary
# for key, value in sorted(new_dict.items()):
#     print(f"{key}: {value}")

# print("--")

# # Printing the sorted original dictionary
# for key, value in sorted(a_dictionary.items()):
#     print(f"{key}: {value}")
