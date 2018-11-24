#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler033

from itertools import combinations
from math import gcd

# Explanation: Consider that we want solutions "n/d = n2/d2".
# Iterate through possible values of n which has N digits.
# Then iterate over N-K possible digits from the digits of n (N choose N-K) to make n2.
# Now, consider n/n2. We must have n/n2 = d/d2 and d must have the digit/s of n that n2 doesn't have.
# The clever step is to iterate through fractions that are equal to n/n2;
# this means divide both n and n2 by g = gcd(n, n2)
# and then multiply both n/g and n2 /g by integer i, which you will iterate.
# If we write n/n2 as an ordered pair (n, n2) then the iteration looks like ((n/g)*i, (n2/g)*i), i += 1,
# and for each iteration of i you check if (n/g)*i has the digits of n that n2 doesn't have.


def make_number(digits):
    """
    input tuple of digits (base 10)
    return int of those digits
    """
    res = 0
    digits = list(digits)
    while digits:
        res *= 10
        res += int(digits.pop(0))
    return res


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


def find_indices(number, digit):
    """
    input number as an iterable of digits
    returns all the indices of the occurrences of digit in number
    """
    indices = []
    for i, n in enumerate(number):
        if n == digit:
            indices.append(i)
    return indices


def remove_digits(n, digits):
    """
    input number and digits to be removed
    output set of numbers that are n without the digits
    """
    res = set()
    res.add(n)
    common_digits = list(digits)
    while common_digits:
        d = common_digits.pop()
        new_res = set()
        for number in res:
            occurrences = find_indices(number, d)
            for i in occurrences:
                if i == 0:
                    new_res.add(number[1:])
                elif i == len(number)-1:
                    new_res.add(number[:i])
                else:
                    new_res.add(number[:i] + number[i + 1:])
        res = new_res
    n_res = []
    for i in res:
        if make_number(i) != 0:
            n_res.append(make_number(i))
    return n_res


def has_digits(number, digits):
    """
    return boolean whether number has digits
    """
    digits = list(digits)
    num = [int(x) for x in str(number)]
    while digits:
        d = digits.pop(0)
        if d in num:
            num.remove(d)
        else:
            return False
    return True


def find_shared_digits(numerator_digits, numerator2_digits):
    """
    returns numerator digits without numerator2 digits
    """
    shared_digits = list(numerator_digits)
    for digit in numerator2_digits:
                shared_digits.remove(digit)
    return shared_digits


def digit_canceling_fractions(N, K):
    """
    Finds numbers such that numerator/denominator = numerator2/denominator2
    numerator and denominator have N digits
    numerator and denominator share K digits
    numerator2 and denominator2 have N-K digits
    returns the sum of all the numerators, sum of all the denominators
    """
    res = set()
    for numerator in range(10**(N-1), 10**N):
        numerator_digits = make_digits(numerator)
        for numerator2_digits in set(combinations(numerator_digits, N-K)):
            numerator2 = make_number(numerator2_digits)
            if numerator2 == 0:
                continue
            g = gcd(numerator, numerator2)
            reduced = (numerator // g, numerator2 // g)
            shared_digits = find_shared_digits(numerator_digits, numerator2_digits)
            if 0 in shared_digits:
                continue
            z = 1
            while len(str(reduced[0]*z)) <= N and len(str(reduced[1]*z)) <= N-K:
                if z == g:
                    z += 1
                    continue
                reduced0_z = reduced[0]*z
                reduced1_z = reduced[1]*z
                if has_digits(reduced0_z, shared_digits):
                    reduced0_z_digits = make_digits(reduced0_z)
                    for denominator2 in remove_digits(reduced0_z_digits, shared_digits):
                        if reduced1_z == denominator2 and denominator2 > numerator2:
                            res.add((numerator, reduced0_z))
                z += 1
    return sum(x[0] for x in res), sum(x[1] for x in res)


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(*digit_canceling_fractions(N, K))
