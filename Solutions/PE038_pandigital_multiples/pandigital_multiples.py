#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler038

# multiply until it's K digits, then check if it's K pandigital

from collections import Counter


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


def make_number(digits):
    """
    input tuple of digits (base 10)
    return int of those digits
    """
    res = 0
    digits = list(digits)
    while digits:
        res *= 10
        res += int(digits.pop(0))
    return res


def pandigital_multiples(n, k):
    res = []
    k_digits = Counter(range(1, k + 1))
    for p in range(2, n):
        p_digits = make_digits(p)
        i = 2
        while len(p_digits) < k:
            p_digits += make_digits(p*i)
            i += 1
        if Counter(p_digits) == k_digits:
            res.append(p)
    return res


if __name__ == '__main__':
    n, k = input().split()
    for num in pandigital_multiples(int(n), int(k)):
        print(num)
