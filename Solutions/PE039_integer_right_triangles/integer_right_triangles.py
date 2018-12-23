#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler039

from collections import defaultdict
from math import gcd

# For m > n, m, n generate primitive Pythagorean triple if m or n even and gcd(m, n) == 1
# For primitive Pythagorean triple all multiples of 2m(m+n) are a perimeter of a right triangle


def integer_right_triangles():
    """
    finds number of solutions for perimeter values less than or equal to n
    returns the number with most solutions
    """
    N = 5*10**6
    perimeters = defaultdict(int)
    n = 1
    while n < N//3 + 1:
        m = n + 1
        p = 2*m*(m+n)
        while p <= N:
            if n % 2 == 0 or m % 2 == 0:
                if gcd(m, n) == 1:
                    i = 1
                    perimeter = i*p
                    while perimeter <= N:
                        perimeters[perimeter] += 1
                        i += 1
                        perimeter = i*p
            m += 1
            p = 2*m*(m+n)
        n += 1
    max = 0
    p = 0
    max_perimeters = dict()
    for perimeter in sorted(perimeters):
        if perimeters[perimeter] >= max:
            if perimeters[perimeter] > max:
                p = perimeter
                max = perimeters[perimeter]
                max_perimeters[perimeter] = p
            elif perimeter < p:
                p = perimeter
                max_perimeters[perimeter] = p
        else:
            max_perimeters[perimeter] = p
    return max_perimeters


if __name__ == '__main__':
    solutions = integer_right_triangles()
    every_solution = dict()
    m = 0
    for i in range(12, 5*10**6+1):
        if i in solutions:
            m = solutions[i]
        every_solution[i] = m
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(every_solution[N])
