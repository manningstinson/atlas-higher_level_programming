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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width attribute """
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height attribute """
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x attribute """
        self.__x = value

    @property
    def y(self):
        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y attribute """
        self.__y = value
