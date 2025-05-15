#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # creating an empty a_dictionary for thr new dictionary
    empty_dic = {}
    # looping through the keys and the values of the dictionary
    # Multiply each value by 2 and append it in the new dictionary
    for key, value in a_dictionary.items():
        empty_dic[key] = value * 2
    return empty_dic
