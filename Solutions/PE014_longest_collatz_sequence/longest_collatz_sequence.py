#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler014


def next_collatz(n):
    """
    input is an integer
    returns next number in collatz sequence
    """
    if n % 2 == 0:
        n >>= 1
    else:
        n = 3*n + 1
    return n


cachesize = 5*10**6
cache = [0]*cachesize
cache[1] = 1


def collatz_sequence_length(n):
    if n == 1:
        return 1
    else:
        global cachesize
        global cache
        if n < cachesize and cache[n] != 0:
            return cache[n]
        m = next_collatz(n)
        res = 1 + collatz_sequence_length(m)
        if n < cachesize:
            cache[n] = res
        return res


def longest_collatz_sequence_so_far(N):
    """
    returns a list where index i is the number less than or equal to i that produces the longest collatz sequence
    """
    longest_so_far = [1]*(N+1)
    i = 2
    m = 1
    m_index = 1
    while i <= N:
        size = collatz_sequence_length(i)
        if size >= m:
            m = size
            m_index = i
        longest_so_far[i] = m_index
        i += 1
    return longest_so_far


if __name__ == '__main__':
    res = longest_collatz_sequence_so_far(5000000)
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(res[n])
