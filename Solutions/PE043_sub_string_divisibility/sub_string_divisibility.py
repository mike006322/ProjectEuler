#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler043

from itertools import permutations


def make_number(digits):
    """
    input tuple of digits
    return int of those digits
    """
    res = ''
    for i in digits:
        res += str(i)
    return int(res)


def pandigital_generator(n):
    """
    generates pandigital numbers using digits 0 to n
    output is tuple of integer digits
    """
    for i in permutations(range(n+1), n+1):
        yield i


def sub_string_divisibility(n):
    """
    outputs sum of pandigital numbers that have the divisibility property
    2, 3, 5, 7, 11, 13, 17
    """
    res = 0
    d = [0, 2, 3, 5, 7, 11, 13, 17]
    # divisibility property: 3 digits starting with i are divisible by d[i]
    for pan_number in pandigital_generator(n):
        i = 1
        sub_string_divisible = True
        while i < n - 1:
            if make_number(pan_number[i:i+3]) % d[i] != 0:
                sub_string_divisible = False
                break
            i += 1
        if sub_string_divisible:
            res += make_number(pan_number)
            # print(make_number(pan_number))
    return res


if __name__ == '__main__':
    print(sub_string_divisibility(int(input())))
