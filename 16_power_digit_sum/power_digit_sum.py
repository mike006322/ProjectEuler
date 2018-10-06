#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler016

def power_digit_sum(n):
    """
    returns the sum of the digits of 2**n
    """
    e = 2**n
    digits = []
    for digit in str(e):
        digits.append(int(digit))
    return sum(digits)

def power_digit_sum_small(n):
    return sum(map(int, str(2 ** int(n))))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(power_digit_sum(n))
