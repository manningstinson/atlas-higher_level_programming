#!/usr/bin/python3
"""
Module 9-student

Defines a class Student that represents a student.

Public instance attributes:
- first_name
- last_name
- age

Public method:
- to_json(self): retrieves a dictionary representation of a Student instance.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student information.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

# # Example usage:
# if __name__ == "__main__":
#     students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

#     for student in students:
#         j_student = student.to_json()
#         print(type(j_student))
#         print(j_student['first_name'])
#         print(type(j_student['first_name']))
#         print(j_student['age'])
#         print(type(j_student['age']))
