#!/usr/bin/python3

for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        if (num1 == 8 and num2 == 9):
            print("{}{}".format(num1, num2))
            break
        print("{}{}".format(num1, num2), end=", ")
