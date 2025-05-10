#!/usr/bin/python3

import sys


def infinite_addition():
    int_input = list(map(int, sys.argv[1:]))

    # initilizing the number to be summed cumutalityvly
    number = 0
    for count in int_input:
        number += count
    print("{}".format(number))


if __name__ == "__main__":
    infinite_addition()
