#!/usr/bin/python3
numbers_list = list(range(100))
formatted_numbers = ", ".join("{:02d}".format(n) for n in numbers_list)
print(formatted_numbers)
