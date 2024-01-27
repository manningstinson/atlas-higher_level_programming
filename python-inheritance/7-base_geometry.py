#!/usr/bin/python3
"""
Module 7-base_geometry

Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Represents the base geometry class.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    # Additional test cases
    bg = BaseGeometry()

    # Test case: Valid integer value
    bg.integer_validator("my_int", 12)

    # Test case: Valid integer value
    bg.integer_validator("width", 89)

    # Test case: Invalid value (not an integer)
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Test case: Invalid value (less than or equal to 0)
    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Additional test cases for various non-integer values
    try:
        bg.integer_validator("age", (4,))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", [3])
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", {3, 4})
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", None)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
