#!/usr/bin/python3

# converting the string to uppercase
def uppercase(str):

    # initilizeing the string
    result = ""

    # If the charachter is between a and z, it is captilized by subtracting 32
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    # one print funtion results one \n in the end by defualt
    print("{}".format(result))
