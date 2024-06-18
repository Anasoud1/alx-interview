#!/usr/bin/python3
'''Prime game'''


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def operation(arr):
    for i in arr:
        if isPrime(i):
            arr = list(filter(lambda x: x % i != 0, arr))
            return arr
    return list(1)


def isWinner(x, nums):
    benWins = 0
    mariaWins = 0

    for i in nums:
        count = 0
        arr = list(range(1, i + 1))
        while len(arr) != 1:
            arr = operation(arr)
            count += 1
        if count % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1
    if benWins > mariaWins:
        return 'Ben'
    elif benWins < mariaWins:
        return 'Maria'
    else:
        return None
