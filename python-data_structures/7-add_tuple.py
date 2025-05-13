#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # initilazing a list of size 2
    my_list = [0, 0]
    # iterating the list in 2 indexes
    for idx in range(2):
        # for each elemnt, assigned it to its repective index
        # if it is out of range, assigned to 0
        a = tuple_a[idx] if idx < len(tuple_a) else 0
        b = tuple_b[idx] if idx < len(tuple_b) else 0
        # concating two elemnts in a new_list
        my_list[idx] = a + b
    # convert the list to tuple
    return tuple(my_list)
