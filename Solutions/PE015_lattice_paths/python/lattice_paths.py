#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler015

from math import factorial


def C(n, k):
    """
    Returns nCk, 'n Choose k', the binomial coefficient
    """
    return factorial(n)//(factorial(k)*factorial(n-k))


def lattice_paths(n, m):
    """
    returns the number of lattice paths in an n by m rectangle
    modulo the mod value
    """
    total = 0
    if m > n:
        m, n = n, m
    for i in range(1, m+1):
        if i == 1:
            total += n + 1
        elif i < n:
            total += C(m-1, i-1) * (2*C(n-1, i-1) + C(n-1, i) + C(n-1, i-2))
        else:
            total += C(m-1, i-1) * (2*C(n-1, i-1) + C(n-1, i-2))
    mod = 10**9 + 7
    return total % mod

# other insight:
# consider a path as combination of verticle(x) and horizontal(y) lines so total ways = (x+y)/x!y! like possible ways to get one from two mango and two orange 4!/2!2!
# There are n+m moves needed to reach from start to end. Out of these n+m moves, any n moves should be towards bottom. That is (n+m) C(n) = (n+m) C(m)


def lattice_paths2(n, m):
    return C(n+m, n) % (10**9+7)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(lattice_paths(n, m))
