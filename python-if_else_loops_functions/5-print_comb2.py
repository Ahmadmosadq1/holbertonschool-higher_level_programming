#!/usr/bin/python3

# Looping from 0 to 100 as 100 will not be included.
# Using Comprhension expression, we loop from 0 to 99

numbers = [f"{count:02d}" for count in range(100)]
print(", ".join(numbers), end="\n")
