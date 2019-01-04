#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler044

# P_n = n(3n-1)/2 = (3n^2 - n)/2
# P_n-K = (n-K)(3(n-K)-1)/2 = (n-K)(3n-3K-1)/2 = n(3n-3K-1)/2 - K(3n-3K-1)/2
# = (3n^2 - 3nK - n - 3nK + 3K^2 + K)/2
# = (3n^2 - 6nK - n + 3K^2 + K)/2
# P_n - P_n-K = (3n^2 - n)/2 - (3n^2 - 6nK - n + 3K^2 + K)/2
# = (3n^2 - n - 3n^2 + 6nK + n - 3K^2 - K)/2
# = (6nK - 3K^2 - K)/2
# Question: for constant K, does (3n^2 - n)/2 = (6nK - 3K^2 - K)/2 have integer solution?
# i.e. 3n^2 + (-6K-1)n + 3K^2 + K = 0 have integer solution?
# 3n^2 + (-6K-1)n + 3K^2 + K = 0 solve for n: n = K or n = K + 1/3
# quadratic formula K-1 +- (((6K-1)**2 - 12(3K**2 + K))**.5)/6


def pentagonal_number(n):
    """
    returns P_n = n(3n-1)/2 = (3n^2 - n)/2
    """
    return (3*n**2 - n)/2


def pentagonal_numbers(N, K):
    """
    returns pentagonal_number(n) for all n < N such that P_n - P_n-K is pentagonal
    """
    pass


if __name__ == '__main__':
    pass
