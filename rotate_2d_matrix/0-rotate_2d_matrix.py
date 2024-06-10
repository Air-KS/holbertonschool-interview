#!/usr/bin/python3
"""
Module used to rotate a matrix 90 degres
"""

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees.
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dim and will not be empty.

    Arguments
    ---------
    - matrix  : matrix
                list of non-negative integers.

    Returns
    -------
    - Nothing. The function modifies the original argument
    """

    # create a replica of the original matrix
    copy = matrix[:]

    for index in range(len(matrix)):

        # extract the i column from the copy
        col = [row[index] for row in copy]

         # place it on the original matrix in reverse order
        matrix[index] = col[::-1]
