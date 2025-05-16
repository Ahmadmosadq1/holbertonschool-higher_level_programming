#!/usr/bin/python3
def best_score(a_dictionary):
    # If no score found, return None
    if not a_dictionary:
        return None
    # we first assume any key and its value is the biggest.
    # We need to first turn them into list so we can index them properly
    keys = list(a_dictionary)
    # Chossing the first value-key pair to be the biggiest
    biggest_key = keys[0]
    biggest_value = a_dictionary[biggest_key]

    # Looping through the keys and values
    for key, value in a_dictionary.items():
        if value > biggest_value:
            biggest_value = value
            biggest_key = key
    return biggest_key
