#!/usr/bin/python3

# using the "ord" funtion to get the ASCII values
for alpha in range(ord('a'), ord('z') + 1):

    # Excluding the letters 'e' and 'q'
    if alpha not in (ord('e'), ord('q')):
        print("{:c}".format(alpha), end="")
