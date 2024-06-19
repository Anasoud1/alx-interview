#!/usr/bin/python3
'''Prime game'''


def isPrime(num):
    '''function that return if a number is prime or not'''
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def operation(arr):
    '''functon that return array after retreiving the primes numbers'''
    for i in arr:
        if isPrime(i):
            arr = list(filter(lambda x: x % i != 0, arr))
            return arr
    return list(1)


def isWinner(x, nums):
    '''function that dertermine the winner'''
    benWins = 0
    mariaWins = 0
    i = 0

    while i < x:
        count = 0
        arr = list(range(1, nums[i] + 1))
        while len(arr) != 1:
            arr = operation(arr)
            count += 1
        if count % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1
        i += 1
    if benWins > mariaWins:
        return 'Ben'
    elif benWins < mariaWins:
        return 'Maria'
    else:
        return None
