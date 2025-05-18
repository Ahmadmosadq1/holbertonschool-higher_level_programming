#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    string = roman_string.upper()
    for i in range(len(string) - 1):
        current = vals.get(string[i], 0)
        next = vals.get(string[i+1], 0)
        if current < next:
            sum -= current
        else:
            sum += current
    sum += vals.get(string[-1], 0)
    return sum
