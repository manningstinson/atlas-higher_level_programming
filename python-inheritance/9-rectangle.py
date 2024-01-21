#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing a base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: If area is not implemented.

        Returns:
            int: The area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
