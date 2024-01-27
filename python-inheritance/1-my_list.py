#!/usr/bin/python3
"""
My List module
"""
class MyList(list):
    """A custom list class that can print its elements in sorted order."""

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        sorted_list = sorted(self)  # Create a temporary sorted copy
        print(sorted_list)

# # Example usage:
# my_list = MyList()
# my_list.append(1)
# my_list.append(4)
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)

# print(my_list)   # Output: [1, 4, 2, 3, 5]
# my_list.print_sorted()  # Output: [1, 2, 3, 4, 5]
# print(my_list)   # Output: [1, 4, 2, 3, 5] (original order preserved)
