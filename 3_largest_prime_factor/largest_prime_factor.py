#!/bin/python3

#https://www.hackerrank.com/contests/projecteuler/challenges/euler003

import sys

# Two important considerations here:
# 1.) First is that if you increment from the smallest prime dividing the primes away from n then the next smallest divisor you find of n will be prime.
# 2.) Second is that if there is a single prime factor greater than sqrt(n) then after the loop n will equal it

def biggest_prime_factor(n):
    max = n
    """test numbers up to square root of n. Divide n by factors as you go to skip over composite numbers"""
    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
        if n == 1:
            return 2
    i = 3
    res = 1
    while i <= max**.5 + 1:
        if n % i == 0:
            # i is prime by 1.)
            res = i
            n /= i
        else:
            i += 2
    if n > 2:
        return int(n)
    # by 2.)
    else:
        return int(res)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(biggest_prime_factor(n))
