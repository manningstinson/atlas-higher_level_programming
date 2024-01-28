#!/usr/bin/python3
"""
Base module
"""

import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method

        Args:
            id (int): object identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert list of dictionaries to JSON string

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            str: JSON representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON representation of list_objs to a file

        Args:
            list_objs (list): List of instances inheriting from Base
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string

        Args:
            json_string (str): JSON string representing a list of dictionaries

        Returns:
            list: List represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes set using the provided dictionary.

        Args:
            **dictionary: Dictionary containing attribute values.

        Returns:
            Base: Instance with attributes set.
        """
        dummy_instance = cls(1)  # Create a dummy instance with arbitrary ID (1)
        dummy_instance.update(**dictionary)  # Update with real values
        return dummy_instance

    def update(self, *args, **kwargs):
        """
        Update instance attributes with values from args and kwargs.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y', 'size'][:len(args)]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the instance.

        Returns:
            dict: Dictionary representing the instance.
        """
        return {key: getattr(self, key) for key in ['id', 'width', 'height', 'x', 'y', 'size']}


class Rectangle(Base):
    """
    Rectangle class, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Object identifier.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for Square

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): Object identifier.
        """
        super().__init__(size, size, x, y, id)


if __name__ == "__main__":
    s1 = Square.create(**{'size': 2})
    print(s1)
