#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # doing a copy so we dont change the original
    # [:] means copying the whole matrix
    copy_matrix = [row[:] for row in matrix]
    # i loops though the lists, j loops through the elemnts of each list
    for i in range(len(copy_matrix)):
        for j in range(len(copy_matrix[i])):
            copy_matrix[i][j] = copy_matrix[i][j] ** 2
    return copy_matrix
