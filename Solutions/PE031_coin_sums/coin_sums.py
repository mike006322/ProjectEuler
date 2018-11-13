#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler031

# Dynamic programming solution


def coin_sums(n):
    """
    input number
    output array from 0 to n the number of ways you can add up to n using coins in (5, 10, 20, 50, 100, 200)
    """
    units = (5, 10, 20, 50, 100, 200)
    table = [x // 2 + 1 for x in range(n+1)]
    table[0] = 1
    for unit in units:
        for i in range(unit, n + 1):
            table[i] += table[i - unit]
    return table


if __name__ == '__main__':
    sums = coin_sums(10**5)
    mod = 10**9 + 7
    t = int(input())
    for _ in range(t):
        print(sums[int(input())] % mod)
