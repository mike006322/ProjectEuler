#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler025

from functools import lru_cache

cache_num_digits = [0]*5001

@lru_cache(maxsize=None)
def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num > 2:
        return fib(num - 1) + fib(num - 2)


@lru_cache(maxsize=None)
def n_digit_fibonacci_number(n):
    """
    calculates index of first fibonacci number containing n digits
    """
    if n == 1:
        return 1
    i = n_digit_fibonacci_number(n - 1)
    k = fib(i)
    while len(str(k)) < n:
        i += 1
        k = fib(i)
    return i + 1



def n_digit_fibonacci_number2(N):
    """
    calculates list of indices of first fibonacci numbers containing n digits up to N
    """
    cache = [0]*50001
    i = 1
    k = fib(i)
    n = 2
    while n <= N:
        while len(str(k)) < n:
            i += 1
            k = fib(i)
        cache[n] = i + 1
        n += 1
    return cache

if __name__ == '__main__':
    cache = n_digit_fibonacci_number2(5000)
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(cache[n])
