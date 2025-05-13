#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # we iterate each list inside the matrix
    for row in matrix:
        # Here, we seperate the elements using join to iterate each list
        # At the end of each loop, print() will add new line
        print(" ".join("{:d}".format(num) for num in row))
