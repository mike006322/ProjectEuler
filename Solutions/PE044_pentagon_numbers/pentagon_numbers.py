#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler044

# P_n = n(3n-1)/2 = (3n^2 - n)/2
# P_n-K = (n-K)(3(n-K)-1)/2 = (n-K)(3n-3K-1)/2 = n(3n-3K-1)/2 - K(3n-3K-1)/2
# = (3n^2 - 3nK - n - 3nK + 3K^2 + K)/2
# = (3n^2 - 6nK - n + 3K^2 + K)/2
# P_n - P_n-K = (3n^2 - n)/2 - (3n^2 - 6nK - n + 3K^2 + K)/2
# = (3n^2 - n - 3n^2 + 6nK + n - 3K^2 - K)/2
# = (6nK - 3K^2 - K)/2
# P_n + P_n-K = (3n^2 - n)/2 + (3n^2 - 6nK - n + 3K^2 + K)/2
# = (3n^2 - n + 3n^2 - 6nK - n + 3K^2 + K)/2
# = (6n^2 - 2n(1 - 3K) + 3K^2 + K)/2
# Question: for constant K, which n's grant that (3m^2 - m)/2 = (6nK - 3K^2 - K)/2 has integer solution?
# 3m^2 - m = 6nK - 3K^2 - K
# 0 = - 3m^2 + m + 6nK - 3K^2 - K
# solving for m:
# -1 +- (1 + 12(6nK - 3K^2 - K))**.5 all over -6
# 1 -+ (1 + 12(6nK - 3K^2 - K))**.5 all over 6
# happens when 1 -+ (1 + 12(6nK - 3K^2 - K))**.5 = 6r for some r
# (1 + 12(6nK - 3K^2 - K))**.5 = 6r +- 1
# 1 + 12(6nK - 3K^2 - K) = (6r +- 1)^2


def pentagonal_number(n):
    """
    returns P_n = n(3n-1)/2 = (3n^2 - n)/2
    """
    return (3*n**2 - n)//2


def is_pentagonal(n):
    """
    returns boolean whether n is a solution to (3*m**2 - m)
    """
    # n = 3*m**2 - m ? for some m
    # 0 = 3*m**2 - m - n
    # (1 +- (1 + 12*n)**.5)/6
    if 1 + 12*n > 1:
        if (1 + (1 + 24*n)**.5)/6 == (1 + (1 + 24*n)**.5)//6:
            return True
    return False


def pentagonal_numbers(N, K):
    """
    returns pentagonal_number(n) for all n < N such that P_n - P_n-K is pentagonal
    """
    for n in range(K+1, N):
        # test whether (3n^2 - n)/2 - (3n^2 - 6nK - n + 3K^2 + K)/2 is pentagonal
        P_n_minus_P_n_K = (6*n*K - 3*K**2 - K)//2
        # if is_pentagonal(P_n_minus_P_n_K):
        #     print(pentagonal_number(n))
        P_n_plus_P_n_K = pentagonal_number(n) + pentagonal_number(n-K)
        # if is_pentagonal(P_n_plus_P_n_K):
        #     print(pentagonal_number(n))
        if is_pentagonal(P_n_minus_P_n_K) and is_pentagonal(P_n_plus_P_n_K):
            print(P_n_minus_P_n_K)


if __name__ == '__main__':
    # pentagonal_numbers(50, 8)
    # pentagonal_numbers(*map(int, input().split()))
    for i in range(1, 9999):
        pentagonal_numbers(10000, i)

