#!/usr/bin/python3

# converting the string to uppercase
def uppercase(str):
    result = ""
    for index, char in enumerate(str):
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result), end="")
    if index == len(str) - 1:
        print()
