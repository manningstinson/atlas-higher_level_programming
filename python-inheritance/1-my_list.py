#!/usr/bin/python3
"""
Module for MyList class.
"""

class MyList(list):
    """
    A class that inherits from list.

    Public instance method:
    - print_sorted(self): prints the list, but sorted in ascending order.

    Example:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
