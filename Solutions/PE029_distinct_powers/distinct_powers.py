#!/bin/python3

#https://www.hackerrank.com/contests/projecteuler/challenges/euler029


def gcd(a,b):
    """
    returns the greatest common divisor of a and b
    """
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    returns the lowest common multiple of a and b
    """
    return a * b // gcd(a, b)


def distinct_powers_naive(n):
    powers = set()
    powers_seen = []
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i**j not in powers:
                powers.add(i**j)
            else:
                powers_seen.append([i, j, i**j])
    return len(powers)


def count_dupes(exp, n):
    """
    returns the number duplicates a number that is a certain power (exp) of another number has
    """
    overlaps = [0] * (n + 1)
    for e in range(1, exp):
        step = lcm(e, exp) // exp
        end = e * n // exp
        for i in range(2*step, end+1, step):
            overlaps[i] = 1
    return sum(overlaps)


def distinct_powers(n):
    """
    input two int's n, n
    returns number of distinct powers, A**B for 1 < A <= n, 1 < B <= n.
    """
    exponents = [1] * (n + 1)
    # modify the list so that all index**value are unique
    for i in range(2, len(exponents)):
        if exponents[i] > 1:
            continue
        e = 2
        while i**e <= n:
            exponents[i**e] = e
            e += 1
    # exponents = [1, 1, 1, 1, 2, 1, 1, 1, 3, 2, 1, ...
    # only index values that are powers of other numbers contain duplicates
    # i.e. if exponents[i] > 1, count the duplicates
    dupes = {exp: count_dupes(exp, n) for exp in exponents if exp > 1}
    exponents = [exp for exp in exponents if exp > 1]
    total_duplicates = 0
    for exp in exponents:
        total_duplicates += dupes.get(exp)
    return (n - 1) * (n - 1) - total_duplicates


if __name__ == '__main__':
    print(distinct_powers(int(input())))
