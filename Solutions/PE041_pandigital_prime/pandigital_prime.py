#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler041

from itertools import permutations


def make_number(digits):
    """
    input tuple of digits
    return int of those digits
    """
    res = ''
    for i in digits:
        res += str(i)
    return int(res)


def is_prime(n):
    """
    Returns boolean whether n is prime
    """
    if n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n**.5:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def make_pandigital_primes(n):
    """
    returns sorted pandigital primes up to length n as dict(# digits: highest pandigital prime)
    """
    res = dict()
    for i in range(4, n+1):
        res[i] = list()
        for digits in permutations(range(1, i+1), i):
            p = make_number(digits)
            if is_prime(p):
                res[i].append(p)
    return res


def binary_search(alist, item):
    """
    returns the index where the item is in alist. O(logn) time
    alist must be in ascending order
    # returns the index of element closest to the item that is still <= item in alist
    """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = alist[midpoint]
        elif alist[midpoint-1] <= item < alist[midpoint]:
            found = alist[midpoint-1]
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


if __name__ == '__main__':
    pandigital_primes = make_pandigital_primes(7)
    t = int(input())
    for _ in range(t):
        n = input()
        if int(n) >= 7652413:
            print(7652413)
        elif 4231 <= int(n) < 1234657:
            print(4231)
        elif int(n) < 1423:
            print(-1)
        else:
            print(binary_search(pandigital_primes[len(n)], int(n)))

    # n = '7642513'
    # if int(n) >= 7652413:
    #     print(7652413)
    # elif 4231 <= int(n) < 1234657:
    #     print(4231)
    # elif int(n) < 1423:
    #     print(-1)
    # else:
    #     print(binary_search(pandigital_primes[len(n)], int(n)))

