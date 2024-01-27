#!/usr/bin/python3
"""
Module 10-student:

Defines a Student class with public instance attributes:
- first_name
- last_name
- age

Public methods:
- __init__(self, first_name, last_name, age):
Instantiates a Student object.
- to_json(self, attrs=None): Retrieves
a dictionary representation of a Student instance.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list of str): A list of attribute names
        to retrieve (default is None).

        Returns:
        - dict: A dictionary containing attribute names and values.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
