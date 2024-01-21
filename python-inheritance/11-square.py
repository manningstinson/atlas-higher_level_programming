#!/usr/bin/python3
"""
Module containing the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        Returns:
            str: String representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def print(self):
        """
        Prints the square description.
        """
        print(self.__str__())


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
