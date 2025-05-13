#!/usr/bin/python3
def element_at(my_list, idx):

    # It is the safest way to check if idx out of range as a first condition
    if idx > len(my_list):
        return None
        # you use "return"  only without None.

    elif my_list[idx] < 0:
        # if the index is negative
        return

    else:
        # if index is out of range:
        return my_list[idx]
