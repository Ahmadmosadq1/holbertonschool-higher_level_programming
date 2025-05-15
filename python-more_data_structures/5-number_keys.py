#!/usr/bin/python3
def number_keys(a_dictionary):
    # We first intiilaize a counter and while we loop the keys, we increase 1
    count = 0
    for key in a_dictionary.keys():
        count += 1
    return count
