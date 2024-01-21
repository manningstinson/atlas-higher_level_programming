#!/usr/bin/python3
"""
Module 10-square.py
Defines a Square class that inherits from Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
        - The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Format: [Square] <width>/<height>

        Returns:
        - String representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
