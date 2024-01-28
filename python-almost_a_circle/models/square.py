#!/usr/bin/python3

""" Square Module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """

        # Call the super class with id, x, y, width, and height
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the object """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update the attributes of the square """

        # Define the order of attributes and their corresponding names
        attr_names = ["id", "size", "x", "y"]

        # Update attributes using positional arguments
        for i, arg in enumerate(args):
            setattr(self, attr_names[i], arg)

        # Update attributes using keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
