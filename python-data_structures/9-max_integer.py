#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == []:
        return
    # Creating a varaible to store the biggest integer
    # we assume the first element is the biggiest one for now
    biggest_int = my_list[0]
    # looping the list
    for idx in range(len(my_list) - 1):
        # comparing each idex with max value
        if my_list[idx] > biggest_int:
            biggest_int = my_list[idx]
    return biggest_int
