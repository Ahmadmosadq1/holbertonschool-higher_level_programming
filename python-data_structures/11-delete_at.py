#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # if index is negative or out of range, return the same list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    del my_list[idx]
    return my_list
