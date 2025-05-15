#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = [row[:] for row in matrix]
    for i in range(len(copy_matrix)):
        for j in range(len(copy_matrix[i])):
            copy_matrix[i][j] = copy_matrix[i][j] ** 2
    return copy_matrix