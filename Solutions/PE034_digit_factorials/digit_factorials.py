#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler034

from math import factorial


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


def digit_factorial(n):
    res = 0
    for i in range(10, n):
        digits = tuple(map(factorial, make_digits(i)))
        if sum(digits) % i == 0:
            res += i
    return res


def digit_factorial_sum(n):
    res = 0
    for i in range(3, n):
        digits = tuple(map(factorial, make_digits(i)))
        if sum(digits) == i:
            res += i
    return res


if __name__ == '__main__':
    n = int(input())
    print(digit_factorial(n))
