#!/usr/bin/python3

# Looping through the decimal and hexa number and arrange them in colums
for number in range(0, 99):
    print("{number:d} = {number:#x}".format(number=number))
