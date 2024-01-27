#!/usr/bin/python3
"""
Module for defining the Student class and
serialization/deserialization methods.
"""


class Student:
    """
    Class representing a student.

    Public instance attributes:
    - first_name
    - last_name
    - age

    Methods:
    - __init__(self, first_name, last_name, age):
    Instantiation method.
    - to_json(self, attrs=None): Retrieves a
    dictionary representation of a Student instance.
    - reload_from_json(self, json): Replaces all
    attributes of the Student instance.

    You can assume json will always be a dictionary.
    A dictionary key will be the public attribute name.
    A dictionary value will be the value of the public attribute.
    You are not allowed to import any module.
    """
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student with the
        given first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes
         name contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in
                self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
         with values from the provided dictionary."""
        self.__dict__.update(json)
