#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-31/challenges/hanging-posters

import math


def solve(h, wallPoints, lengths):
    max_ladder_length = 0
    for i, wallPoint in enumerate(wallPoints):
        ladder_length = math.ceil(wallPoint - .25*lengths[i] - h)
        if ladder_length > max_ladder_length:
            max_ladder_length = ladder_length
    return max_ladder_length


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    h = int(first_multiple_input[1])
    wallPoints = list(map(int, input().rstrip().split()))
    lengths = list(map(int, input().rstrip().split()))
    print(solve(h, wallPoints, lengths))
