#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """

        # Call the super class with id
        super().__init__(id)

        # Private instance attributes with public getter and setter
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and return the area of the Rectangle """
        return self.width * self.height

    def display(self):
        """ Display the Rectangle instance using '#' """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ Override __str__ method to return formatted string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
