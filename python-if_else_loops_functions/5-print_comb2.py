#!/usr/bin/python3

# Looping from 0 to 100 as 100 will not be included.

for count in range(100):
    print(f"{count:02d}", end=", " if count < 99 else "\n")
