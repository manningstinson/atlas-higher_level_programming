#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = " ".join(["{:5d}".format(num) for num in row])
        print(formatted_row)
