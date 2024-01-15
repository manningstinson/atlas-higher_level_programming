#!/usr/bin/python3
"""
Module 7-rectangle

Defines a Rectangle class with private instance attributes, properties,
class attributes, and various methods for manipulation.
"""

class Rectangle:
    """
    Rectangle class with private attributes, properties, and methods.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using the print_symbol."""
        return "\n".join([str(Rectangle.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

# # Example usage
# if __name__ == "__main__":
#     my_rectangle_1 = Rectangle(8, 4)
#     print(my_rectangle_1)
#     print("--")
#     my_rectangle_1.print_symbol = "&"
#     print(my_rectangle_1)
#     print("--")

#     my_rectangle_2 = Rectangle(2, 1)
#     print(my_rectangle_2)
#     print("--")
#     Rectangle.print_symbol = "C"
#     print(my_rectangle_2)
#     print("--")

#     my_rectangle_3 = Rectangle(7, 3)
#     print(my_rectangle_3)
#     print("--")

#     my_rectangle_3.print_symbol = ["C", "is", "fun!"]
#     print(my_rectangle_3)
#     print("--")

#     print("Number of instances:", Rectangle.number_of_instances)
#     del my_rectangle_1
#     print("Number of instances:", Rectangle.number_of_instances)
#     del my_rectangle_2
#     print("Number of instances:", Rectangle.number_of_instances)
