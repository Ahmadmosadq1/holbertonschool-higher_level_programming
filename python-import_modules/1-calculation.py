#!/usr/bin/python3

# since we will be using all the funtions, no need to use "from"
import calculator_1

# making a gaurd for the library
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} == {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} == {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} == {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} == {}".format(a, b, calculator_1.div(a, b)))
