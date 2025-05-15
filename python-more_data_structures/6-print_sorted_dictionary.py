#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Looping keys and values in the sotred dictionary
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
