#!/usr/bin/python3

# Looping through the decimal and hexa number and arrange them in colums
for number in range(0,99):
    print("{number:3d} = {number:3#X}".format(number, number))

