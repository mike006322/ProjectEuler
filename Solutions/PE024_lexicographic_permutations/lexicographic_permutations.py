#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler024

from math import factorial

'abcdefghijklm'

# convert to factorial number system

def find_largest_factorial(n):
    """
    returns i, where factorial(i) >= n
    """
    if n == 0:
        return 0
    i = 1
    k = 1
    while k <= n:
        i += 1
        k = factorial(i)
    else:
        return i - 1

def convert_to_factorial_base(n):
    """
    input is int
    output is a list corresponding to factorial base
    [2, 1, 0] = 0*0! + 1*1! + 2*2! = 0 + 1 + 4 = 5
    """
    i = find_largest_factorial(n)
    res = []
    while i > 0:
        s = 0
        while n >= factorial(i):
            n -= factorial(i)
            s += 1
        res.append(s)
        i -= 1
    return res + [0]

def convert_to_factorial_base_13(n):
    """
    input is int less than 14!
    output is a list corresponding to factorial base 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0] = 0*0! + 1*1! + 2*2! = 0 + 1 + 4 = 5
    """
    i = find_largest_factorial(n)
    res = []
    while i > 0:
        s = 0
        while n >= factorial(i):
            n -= factorial(i)
            s += 1
        res.append(s)
        i -= 1
    res += [0]
    res = (13 - len(res))*[0] + res
    return res

def permute_by_factorialized_index(word, index):
    """
    input is an ordered word to be permuted and a factorial number
    """
    res = ''
    for i in index:
        res += word[i]
        if i < len(word):
            word = word[:i] + word[i+1:]
        else:
            word = word[:i]
    return res

if __name__ == '__main__':
    index = convert_to_factorial_base(1000000 - 1)
    print(permute_by_factorialized_index('0123456789', index))
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     index = convert_to_factorial_base_13(n - 1)
    #     print(permute_by_factorialized_index('abcdefghijklm', index))
