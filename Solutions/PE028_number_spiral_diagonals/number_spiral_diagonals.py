#!/bin/python3


def number_spiral_diagonals(n):
    mod = 1000000007
    return ((n*(n+1)*(2*n+1))//3 - ((n-1)*(n-1))//2 - 1) % mod


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(number_spiral_diagonals(int(input())))
