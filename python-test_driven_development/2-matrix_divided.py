#!/usr/bin/python3
"""
This module has a function that takes 2 args.
one is the matrix and the other is the diivider (div)
it divides the matrix by div
taking into account all the exception errors like TypeErrors..etc
"""


def matrix_divided(matrix, div):
    """ Divider function that takes 2 arguments matrix and div.

        Args:
        matrix: list of lists of numbers(integer or float)
        div: The divider (non zero)

    Returns:
        list: tnew_list

    Raises:
        "TypeError": if matrix is not list of list
        or rows are not the same length
        or the numbers are not float or int

        "ZeroDivisionError": If div = 0

    """
    if (
        not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(
            isinstance(element, (int, float))
            for row in matrix for element in row)
       ):
        text = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(text)
    if not matrix:
        return []
    row_list = len(matrix[0])
    if not all(len(row) == row_list for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[i])):
            result = round(matrix[i][j]/div, 2)
            temp_list.append(result)
        new_list.append(temp_list)

    return new_list
