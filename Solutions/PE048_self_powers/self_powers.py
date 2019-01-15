#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler048


def self_powers(n):
    """
    returns (1^1 + 2^2 + ... + n^n) % 10^10
    """
    res = 0
    mod = 10**10
    for i in range(1, n+1):
        res += pow(i, i, mod)
        # res += i**i % mod
        res %= mod
    return res


if __name__ == '__main__':
    print(self_powers(int(input())))
