#!/usr/bin/python3
"""
Module: 4-from_json_string

Contains a function to convert a JSON string to a Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: Python data structure representing the JSON string.
    """
    return json.loads(my_str)

# # Example usage
# if __name__ == "__main__":
#     s_my_list = "[1, 2, 3]"
#     my_list = from_json_string(s_my_list)
#     print(my_list)
#     print(type(my_list))

#     s_my_dict = """
#     {"is_active": true, "info": {"age": 36, "average": 3.14},
#     "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
#     """
#     my_dict = from_json_string(s_my_dict)
#     print(my_dict)
#     print(type(my_dict))

#     try:
#         s_my_dict_error = """
#         {"is_active": true, 12 }
#         """
#         my_dict_error = from_json_string(s_my_dict_error)
#         print(my_dict_error)
#         print(type(my_dict_error))
#     except json.JSONDecodeError as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
