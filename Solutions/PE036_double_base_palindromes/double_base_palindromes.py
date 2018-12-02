#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler036


def convert_to_base_k(n, k):
    """
    returns string representation of integer n in base k numbering system
    """
    res = ''
    while n:
        res = str(n % k) + res
        n = n // k
    return res


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


def is_palindrome(digits):
    """
    return boolean whether digits is palindrome
    """
    d_len = len(digits)
    if d_len % 2 == 0:
        a = list(digits)
        b = list()
        while len(a) > d_len // 2:
            b.append(a.pop())
        if a == b:
            return True
        else:
            return False
    else:
        a = list(digits)
        a.pop((len(a)//2))
        b = list()
        while len(a) > d_len // 2:
            b.append(a.pop())
        if a == b:
            return True
        else:
            return False


def double_base_palindrome(n, k):
    """
    returns the sum of all the number less than n that are palindromes in base 10 and binary
    """
    res = 0
    for i in range(1, n):
        if is_palindrome(make_digits(i)):
            if is_palindrome(make_digits(convert_to_base_k(i, k))):
                res += i
    return res


if __name__ == '__main__':
    n, k = input().split()
    print(double_base_palindrome(int(n), int(k)))
