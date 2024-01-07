#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0  # Counter for the number of integers printed
    index = 0  # Index to access elements in the list

    try:
        while count_integers < x:
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end=' ')
                count_integers += 1
            index += 1
    except IndexError:
        pass  # Ignore the IndexError when x is greater than the length of my_list
    finally:
        print()  # Print a new line after printing integers
        return count_integers

# Example usage:
my_list = [1, 2, 'hello', 3, 'world', 4]
x = 4
result = safe_print_list_integers(my_list, x)
print("Number of integers printed:", result)
