#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen


def mean_remaining(numbers, n):
    if n == 0:
        return 10**7
    return float(sum(numbers)) / n


def solve(n, a):
    K = len(a)
    if n == K:
        return min(a)
    a = sorted(a, reverse=True)
    if K == 1:
        return a[0]
    while mean_remaining(a[1:], n-1) < a[0]:
        a.pop(0)
        n -= 1
    return mean_remaining(a, n)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    print(solve(n, a))
