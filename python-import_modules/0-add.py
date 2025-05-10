#!/usr/bin/python3

# importing add funtion from the module add0
from add_0 import add

# By default, when you import a module in a main file, it execute all lines
# To ensure thia does not happen, we have to make a gaurd condition
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
