#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-31/challenges/basketball-tournament-1

# unfinished due to time

from itertools import permutations

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY h
#  4. 2D_INTEGER_ARRAY rounds
#


def P(h):
    res = 0
    for p in permutations(h):
        res += sum(p)


def solve(n, m, h, rounds):
    # find minimal K
    K = 0
    # start by looking at all n players, compute P if not, lower number of players to look at
    # n -= 1
    # look at consecutive n number of players, determine P
    # if it doesn't work for n = 1, then return -1


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    h = list(map(int, input().rstrip().split()))
    rounds = []
    for _ in range(m):
        rounds.append(list(map(int, input().rstrip().split())))
    solve(n, m, h, rounds)

