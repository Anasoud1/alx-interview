#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """fuction that rotate matrix 90 degrees clockwise."""
    new = []
    for mat in matrix:
        for m in mat:
            new.append(m)
    new.reverse()
    size = len(matrix)
    n = size
    k = n - 1
    i = 0
    while i < size:
        j = 0
        while j < size:
            matrix[i][j] = new[k]
            k += size
            j += 1
        n -= 1
        k = n - 1
        i += 1
