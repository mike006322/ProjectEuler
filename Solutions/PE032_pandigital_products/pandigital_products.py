#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler032

from itertools import combinations
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

def max_digit_length(n):
    """
    input number of digits
    output the max number of digits the first number can be
    """
    if n == 4:
        return 1
    if n == 5:
        return 1
    if n == 6:
        return 1
    if n == 7:
        return 2
    if n == 8:
        return 2
    if n == 9:
        return 2


def pandigitial_products(n):
    res = set()
    set_of_digits = {x for x in range(1, n+1)}
    m = max_digit_length(n)
    for digits in (x for l in range(1, m + 1) for x in combinations(set_of_digits, l)):
        unused_digits = set(set_of_digits)
        for i in digits:
            unused_digits.remove(i)
        for other_digits in (x for l in range(1, n//3 + 2) for x in combinations(unused_digits, l)):
            product_digits = set(unused_digits)
            for i in other_digits:
                product_digits.remove(i)
            for x in permutations(digits, len(digits)):
                for y in permutations(other_digits, len(other_digits)):
                    for z in permutations(product_digits, len(product_digits)):
                        if make_number(x) * make_number(y) == make_number(z):
                            res.add(make_number(z))
    return sum(res)


if __name__ == '__main__':
    print(pandigitial_products(int(9)))
