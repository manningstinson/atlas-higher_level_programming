#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []
    
    # Iterate through the elements of the original list
    for element in my_list:
        # Replace occurrences of 'search' with 'replace'
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    
    return new_list

# # Example usage:
# original_list = [1, 2, 3, 4, 2, 5]
# result_list = search_replace(original_list, 2, 10)
# print(result_list)
