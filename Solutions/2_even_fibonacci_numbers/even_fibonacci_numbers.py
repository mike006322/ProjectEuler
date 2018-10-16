#!/bin/python3

# #https://www.hackerrank.com/contests/projecteuler/challenges/euler002

import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num > 2:
        return fib(num - 1) + fib(num - 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    even_fib_lessthan_n = []
    i = 1
    fib_i = 1
    while fib_i < n:
        if fib_i % 2 == 0:
            even_fib_lessthan_n.append(fib_i)
        i += 1
        fib_i = fib(i)
    print(sum(even_fib_lessthan_n))

#for i in range(6):
    #print(fib(i))
