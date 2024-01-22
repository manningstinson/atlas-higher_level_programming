#!/usr/bin/python3
""" Module for class to JSON serialization
"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.

    """

    # Get the dictionary representation of the object's attributes
    obj_dict = obj.__dict__

    # Convert any nested objects to dictionaries recursively
    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)

    return obj_dict


# if __name__ == "__main__":
    # # Test cases
    # MyClass = __import__('8-my_class').MyClass
    # m = MyClass("John")
    # m.number = 89
    # print(type(m))
    # print(m)

    # mj = class_to_json(m)
    # print(type(mj))
    # print(mj)
