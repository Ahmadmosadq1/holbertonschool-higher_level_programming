#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Creating an empty list
    new_list = []

    # lopping through my_list indexes to append to new_lsit
    for idx in my_list:
        # using insert method to always insert the elemnt @ 0 position
        new_list.insert(0, idx)
    # lopping theough the new_list which was reversed
    for new_idx in new_list:
        print("{:d}".format(new_idx))
