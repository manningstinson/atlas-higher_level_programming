#!/usr/bin/python3
#!/usr/bin/python3
import random

for _ in range(1):
    number = random.randint(-10, 10)
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
