#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format
        (self.id, self.x, self.y, self.width)

    def area(self):
        """Return the area of the Square"""
        return self.width * self.height

    # Additional methods or overrides can be added here if needed

# if __name__ == "__main__":
#     # Example usage as described in the prompt
#     s1 = Square(2)
#     print(s1)
#     if str(s1) != "[Square] (1) 0/0 - 2":
#         print("Error in __str__ method for Square class")
