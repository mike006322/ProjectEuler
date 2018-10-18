#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler026

def division_algorithm(n, m):
    """
    input integers n, m
    returns n//m, n - m*(n//m)
    """
    if m > n:
        return 0, n
    q = n//m
    return q, n - m*q

def find_cycle_length(d):
    """
    input integer
    output integer representing the length of the cycle of repeating digits in 1/d
    """
    seen = set()
    k = 1
    has_cycle = False
    cycle_length = 0
    look_for = None
    found_cycle = False
    while not has_cycle and k != 0:
        k *= 10
        q, r = division_algorithm(k, d)
        if r == look_for:
            has_cycle = True
        if found_cycle:
            cycle_length += 1
        if r in seen and not found_cycle:
            found_cycle = True
            look_for = r
        seen.add(r)
        k = r
    return cycle_length

def reciprocal_cycles(n):
    """
    input integer n
    output list of smallest number d that has largest cycle length of numbers up to n
    """
    res = [0]*(n+1)
    max_length = 0
    d = 0
    for i in range(1, n + 1):
        cycle_length = find_cycle_length(i)
        if cycle_length > max_length:
            max_length = cycle_length
            d = i
        res[i] = d
    return res


if __name__ == '__main__':
    cycles = reciprocal_cycles(10000)
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(cycles[N-1])
