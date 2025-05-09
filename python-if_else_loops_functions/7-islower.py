#!/usr/bin/python3

# Defining a funtion
def islower(c):
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False
