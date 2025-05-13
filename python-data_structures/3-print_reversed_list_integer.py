#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Creating an empty list
    new_list = []
    # lopping through my_list indexes
    for idx in my_list:
        # using insert method to insert each idx at 0 position
        new_list.insert(0, idx)
    print("{:d}".format(new_list))
