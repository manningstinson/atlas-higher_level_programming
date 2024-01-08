#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict

# # Example Usage:
# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# new_dict = multiply_by_2(a_dictionary)

# # Printing the sorted original dictionary
# for key, value in sorted(a_dictionary.items()):
#     print(f"{key}: {value}")

# print("--")

# # Printing the sorted dictionary after multiplication
# for key, value in sorted(new_dict.items()):
#     print(f"{key}: {value}")
