#!/usr/bin/python3
def safe_print_integer(value):
    # I actually had to run the code without Try/except so i can find 
    # the error when i put a string input
    # if the code seceesed, excute the "try" block, otherwise, excpet block
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
