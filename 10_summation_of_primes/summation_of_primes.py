#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler010

# This solution is correct but not fast enough
# Number of test cases can be up to 10^4
# Better solution is to build the sieve once up to 10^6, then construct table with the sums
# See fast_summation.py for that implementation

def Sieve_of_Eratosthenes(n):
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

def summation_of_primes(n):
    primes = Sieve_of_Eratosthenes(n)
    return sum(primes)

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(summation_of_primes(n))
