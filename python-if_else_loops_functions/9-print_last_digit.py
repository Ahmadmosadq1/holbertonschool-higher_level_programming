#!/usr/bin/python3

def print_last_digit(number):
    
    # number % 10 operation gets the last digit
    last_digit = abs( number)  % 10
    print("{}".format(last_digit), end="")
    return last_digit
