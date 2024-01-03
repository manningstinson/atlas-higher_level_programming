#!/usr/bin/python3
import random

number = random.randint(-10, 10)
print(f"Number: {number}", end=' ')
print(f"is positive" if number > 0 else f"is zero" if number == 0 else f"is negative")
