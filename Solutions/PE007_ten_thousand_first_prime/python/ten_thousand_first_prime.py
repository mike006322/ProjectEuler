#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler007


def sieve_of_eratosthenes(n):
    """
    Return list of primes less than n
    """
    res = [2]
    i = 3
    marked = set()
    while i <= n**.5:
        if i not in marked:
            res.append(i)
            j = 0
            while j <= n/i:
                marked.add(i + j*i)
                j += 1
        i += 2
    while i <= n:
        if i not in marked:
            res.append(i)
        i += 2
    return res


if __name__ == '__main__':
    first_10000_primes = sieve_of_eratosthenes(104729)
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(first_10000_primes[n-1])
