#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler020

# principle is that every time you have a 5*2 as a factor then it yields the same digits as without

from math import factorial

def factorial_digit_sum(N):
    product = factorial(N)
    return sum(tuple(map(int, str(product))))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(factorial_digit_sum(n))
