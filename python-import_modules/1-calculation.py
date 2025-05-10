#!/usr/bin/python3

# since we will be using all the funtions, no need to use "from"
from  calculator_1 import add, sub, mul, div

# making a gaurd for the library
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
