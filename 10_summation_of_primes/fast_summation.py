#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler010

def prime_sums(n):
    """
    Return list of len = n + 1
    index i is the sum of primes less than i
    uses Sieve of Eratosthenes to find primes
    """
    marks = [True]*(n + 1)
    i = 3
    while i <= n**.5:
        if marks[i] == True:
            j = 1
            while i + j*i <= n:
                marks[i + j*i] = False
                j += 1
        i += 2
    marks[1] = 0
    marks[0] = 0
    if n > 1:
        s = 2
        marks[2] = 2
    else:
        s = 0
    for i in range(3, n+1):
        if i%2 == 0:
            marks[i] = False
        if marks[i] == True:
            s += i
            marks[i] = s
        else:
            marks[i] = s
    return marks


if __name__ == '__main__':
    # print(prime_sums(11))
    sums = prime_sums(1000000)
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sums[n])
