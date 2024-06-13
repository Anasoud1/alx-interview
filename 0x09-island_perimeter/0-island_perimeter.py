#!/usr/bin/python3
"""
Perimeter of the island
"""


def island_perimeter(grid):
    '''function that returns the perimeter of the island described in grid'''
    h = len(grid)
    w = len(grid[0])
    p = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    p += 1
                if j + 1 >= w or grid[i][j + 1] == 0:
                    p += 1
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    p += 1
                if i + 1 >= h or grid[i + 1][j] == 0:
                    p += 1
    return p
