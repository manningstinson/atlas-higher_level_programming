#!/usr/bin/python3
"""
Module to save objects to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using JSON representation.

    :param my_obj: The object to be saved.
    :param filename: The name of the file to save the JSON representation.
    """
    with open(filename, 'w') as file:
        if isinstance(my_obj, set):
            my_obj = list(my_obj)
        json.dump(my_obj, file)

# # Example usage
# if __name__ == "__main__":
#     filename = "my_list.json"
#     my_list = [1, 2, 3]
#     save_to_json_file(my_list, filename)

#     filename = "my_dict.json"
#     my_dict = {
#         'id': 12,
#         'name': "John",
#         'places': ["San Francisco", "Tokyo"],
#         'is_active': True,
#         'info': {
#             'age': 36,
#             'average': 3.14
#         }
#     }
#     save_to_json_file(my_dict, filename)

#     try:
#         filename = "my_set.json"
#         my_set = {132, 3}
#         save_to_json_file(my_set, filename)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
