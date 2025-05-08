#!/usr/bin/python3

# Looping from 0 to 100 as 100 will not be included.
# If count reached the last number (i.e 99), it prints newline.
for count in range(00, 100):
    if count == 99:
        print("{:02d}".format(count), end="\n")
        break
    print("{:02d}, ".format(count), end="")
