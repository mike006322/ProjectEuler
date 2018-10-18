#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler014

#idea: instead of caching everything, instead precompute and cache the first some thousand

from functools import lru_cache

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
cache = [0]*(cachesize)
cache[1] = 1

#@lru_cache(maxsize=None)
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

# -------------- The functions below this line are too slow or use too much memory ------------------

def longest_collatz_sequence_so_far2(N):
    """
    returns a list where index i is the number less than or equal to i that produces the longest collatz sequence
    """
    length = [0]*(N+1)
    length[1] = 1
    longest_so_far = [1]*(N+1)
    i = 2
    m = 1
    m_index = 1
    while i <= N:
        b = i
        size = 0
        while b >= 1:
            if length[b] != 0:
                size += length[b]
                break
            size += 1
            b = next_collatz(b)
        length[i] = size
        if size >= m:
            m = size
            m_index = i
        longest_so_far[i] = m_index
        i += 1
        print(size)
    return longest_so_far

def longest_collatz_sequence_so_far3(N):
    """
    returns a list where index i is the number less than or equal to i that produces the longest collatz sequence
    """
    cache = [0]*(7000000)
    cache[1] = 1
    longest_so_far = [1]*(N+1)
    i = 2
    m = 1
    m_index = 1
    while i < 7000000 and i <= N:
        b = i
        size = 0
        while b >= 1:
            if b < 7000000:
                if cache[b] != 0:
                    size += cache[b]
                    break
            size += 1
            b = next_collatz(b)
        cache[i] = size
        if size >= m:
            m = size
            m_index = i
        longest_so_far[i] = m_index
        i += 1
    while i <= N:
        b = i
        size = 0
        while b >= 1:
            if b < 7000000:
                if cache[b] != 0:
                    size += cache[b]
                    break
            size += 1
            b = next_collatz(b)
        if size >= m:
            m = size
            m_index = i
        longest_so_far[i] = m_index
        i += 1
    return longest_so_far

def longest_collatz_sequence(N):
    length = dict()
    length[1] = 1
    i = 2
    m = 1
    while i <= N:
        b = i
        size = 0
        while b > 1:
            if b in length:
                size += length[b]
                break
            size += 1
            b = next_collatz(b)
        length[i] = size
        if size > m:
            m = i
        i += 1
    print(length[9], length[10])
    return m


if __name__ == '__main__':
    # print(len(longest_collatz_sequence_so_far3(100000)))
    res = longest_collatz_sequence_so_far(5000000)
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     print(res[n])
