#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through the rows of the matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through the elements of the row
        for element in row:
            # Check if the element is an integer
            if isinstance(element, int):
                # Square the integer value and add to the result row
                result_row.append(element ** 2)
            else:
                # If not an integer, add the element as it is to the result row
                result_row.append(element)

        # Add the result row to the result matrix
        result_matrix.append(result_row)

    return result_matrix

# # Example usage:
# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = square_matrix_simple(input_matrix)
# print(result)
