#!/usr/bin/python3

"""
Module: 1-my_list

This module defines the MyList class, which inherits from the built-in list class.
It provides a public instance method print_sorted() that prints the list in ascending order.

Usage:
Example usage is demonstrated at the end of the file.

Note:
This module does not import any external modules.
"""

class MyList(list):
    """
    MyList class inherits from the built-in list class.

    Public methods:
    - print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)


# # Example usage
# if __name__ == "__main__":
#     my_list = MyList()
#     my_list.append(1)
#     my_list.append(4)
#     my_list.append(2)
#     my_list.append(3)
#     my_list.append(5)

#     print(my_list)
#     my_list.print_sorted()
#     print(my_list)
