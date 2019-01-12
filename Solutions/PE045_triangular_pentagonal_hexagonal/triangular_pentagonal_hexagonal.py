#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler045


def hexagonal_number(n):
    """
    return nth hexagonal number
    """
    return n*(2*n-1)


def pentagonal_number(n):
    """
    returns nth pentagonal number
    """
    return n*(3*n - 1)//2


def is_pentagonal(n):
    """
    returns boolean whether n is a solution to (3*m**2 - m)
    """
    # n = 3*m**2 - m ? for some m
    # 0 = 3*m**2 - m - n
    # (1 +- (1 + 12*n)**.5)/6
    if (1 + (1 + 24*n)**.5) % 6 == 0:
        return True
    return False


def is_triangular(n):
    """
    returns boolean whether n is a triangular number,
    i.e. whether there exits m such that n = m(m+1)/2 >> 0 = -m^2 - m + 2n
    """
    # m = (- 1 -+ (1 + 8n)**.5)/2
    if (- 1 + (1 + 8*n)**.5) % 2 == 0:
        return True


def triangular_pentagonal_hexagonal(n, a, b):
    nums = {a, b}
    if 6 in nums:
        i = 1
        j = 1
        while i < n:
            j += 1
            if is_pentagonal(i):
                print(i)
            i = hexagonal_number(j)
    elif 3 in nums:
        i = 1
        j = 1
        while i < n:
            j += 1
            if is_triangular(i):
                print(i)
            i = pentagonal_number(j)


if __name__ == '__main__':
    # triangular_pentagonal_hexagonal(*map(int, input().split()))
    j = 1
    for j in range(1, 100000):
        i = hexagonal_number(j)
        if is_pentagonal(i) and is_triangular(i):
            print(i)
