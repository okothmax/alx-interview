#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """
    Create a function that performs an in-place 90-degree
    clockwise rotation of a given n x n 2D matrix.
    The function should not return any value,
    as it should directly modify the input matrix.
    It can be assumed that the input matrix will
    have two dimensions and will not be empty.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
