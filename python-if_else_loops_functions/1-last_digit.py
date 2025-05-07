#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# We need to first convert the number to a string
# So it can be indexed. then we get the last element.
# Then, we convert the last element to integer and compare.
num_str = str(number)
last_digit = int(num_str[-1])


if number <0 or last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")

elif last_digit ==  0:
    print(f"Last digit of {number} is {last_digit} and is 0")

