#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    '''function that return fewest number of coins needed to meet a
    given amount total.'''
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
            if total == 0:
                return change
    return -1
