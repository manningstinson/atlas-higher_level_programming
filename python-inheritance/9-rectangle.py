#!/usr/bin/python3
"""
Module 9-rectangle
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# # Test the implementation
# if __name__ == "__main__":
#     r = Rectangle(3, 5)
#     print(r)
#     print(r.area())
