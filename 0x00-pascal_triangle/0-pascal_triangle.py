#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    new = []
    array = [1]
    if type(n) is not int or n <= 0:
        return []
    for i in range(n):
        line = [1]
        for j in range(i):
            if len(array) > 1 and j != 0:
                line.append(array[j] + array[j-1])
        if i != 0:
            line.append(1)
        new.append(line)
        array = line
    return new
