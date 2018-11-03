#!/bin/python3

# #https://www.hackerrank.com/contests/projecteuler/challenges/euler002

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    """
    returns the nth fibonacci number
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fib(n - 1) + fib(n - 2)


def even_fibonacci_numbers(n):
    """
    returns the sum of the even valued fibonacci numbers less than or equal to n
    """
    even_fib_less_than_n = []
    i = 1
    fib_i = 1
    while fib_i <= n:
        if fib_i % 2 == 0:
            even_fib_less_than_n.append(fib_i)
        i += 1
        fib_i = fib(i)
    return sum(even_fib_less_than_n)


if __name__ == '__main__':
    print(even_fibonacci_numbers(4000000))
    # t = int(input().strip())
    # for a0 in range(t):
    #     n = int(input().strip())
    #     even_fib_lessthan_n = []
    #     i = 1
    #     fib_i = 1
    #     while fib_i <= n:
    #         if fib_i % 2 == 0:
    #             even_fib_lessthan_n.append(fib_i)
    #         i += 1
    #         fib_i = fib(i)
    #     print(sum(even_fib_lessthan_n))
