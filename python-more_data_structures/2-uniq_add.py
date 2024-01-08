#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for num in my_list:
        if isinstance(num, int):  # Check if the element is an integer
            unique_integers.add(num)

    # Sum the unique integers and return the result
    return sum(unique_integers)

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 3, 'not_an_integer', 6]
result = uniq_add(my_list)
print(result)
