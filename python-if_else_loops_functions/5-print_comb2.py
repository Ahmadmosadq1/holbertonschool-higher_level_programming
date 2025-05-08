#!/usr/bin/python3

# Looping from 0 to 100 as 100 will not be included.

for count in range(100):
    print("{:02d}".format(count), end=", " if count < 99 else "\n")
