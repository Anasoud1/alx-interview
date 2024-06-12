#!/usr/bin/python3
"""
Perimeter of the island
"""


def island_perimeter(grid):
    '''function that returns the perimeter of the island described in grid'''
    h = len(grid)
    w = len(grid[0])
    i = 0
    p = 0
    while i < h:
        j = 0
        while j < w:
            if grid[i][j] == 1:
                if (grid[i][j - 1] == 0 and grid[i][j + 1] == 0
                   and grid[i - 1][j] == 0 and grid[i + 1][j] == 0):
                    p = 4
                    break
                elif (grid[i][j - 1] == 0 and grid[i][j + 1] == 0
                      and grid[i - 1][j] == 0):
                    p += 3
                elif (grid[i][j - 1] == 0 and grid[i][j + 1] == 0
                      and grid[i + 1][j] == 0):
                    p += 3
                elif (grid[i][j - 1] == 0 and grid[i + 1][j] == 0
                      and grid[i - 1][j] == 0):
                    p += 3
                elif (grid[i][j + 1] == 0 and grid[i + 1][j] == 0
                      and grid[i - 1][j] == 0):
                    p += 3
                elif (grid[i][j - 1] == 0 and grid[i][j + 1] == 1
                      and grid[i - 1][j] == 1 and grid[i + 1][j] == 1):
                    p += 1
                elif (grid[i][j - 1] == 1 and grid[i][j + 1] == 0
                      and grid[i - 1][j] == 1 and grid[i + 1][j] == 1):
                    p += 1
                elif (grid[i][j - 1] == 1 and grid[i][j + 1] == 1
                      and grid[i - 1][j] == 0 and grid[i + 1][j] == 1):
                    p += 1
                elif (grid[i][j - 1] == 1 and grid[i][j + 1] == 1
                      and grid[i - 1][j] == 1 and grid[i + 1][j] == 0):
                    p += 1
                else:
                    p += 2
            j += 1
        i += 1
    return p
