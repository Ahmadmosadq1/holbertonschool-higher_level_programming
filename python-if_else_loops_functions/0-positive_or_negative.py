#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# If the number is larger than 0, print it is positive.
if number > 0:
    print("{} is positive".format(number))

# If number is smaller than 0, print it is negative.
if number < 0:
    print(f"{number} is negative")

# If number is zero, print is zero
if number == 0:
    print(f"{number} is zero")
