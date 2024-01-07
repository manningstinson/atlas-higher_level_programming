#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0  # Counter for the number of integers printed

    try:
        for value in my_list:
            if count_integers < x and isinstance(value, int):
                print("{:d}".format(value), end="")
                count_integers += 1
    except IndexError:
        # Ignore the IndexError when x is greater than the length of my_list
        pass
    finally:
        print()  # Print a new line after printing integers
        return count_integers

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# nb_print = safe_print_list_integers(my_list, 2)
# print("nb_print: {:d}".format(nb_print))

# my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
# nb_print = safe_print_list_integers(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))

# nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))
