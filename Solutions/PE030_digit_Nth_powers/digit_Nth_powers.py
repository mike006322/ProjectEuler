#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler030

from itertools import combinations_with_replacement
from collections import Counter


def find_max_number_of_digits(power):
    m = 30
    while m*9**power < 10**m:
        m -= 1
    return m + 1


def sum_power(n, combination):
    """
    returns the sum of the ints in combination to the nth power
    """
    sum = 0
    for i in combination:
        sum += i**n
    return sum


def same_number_of_digits(comb_sum, comb):
    """
    input int and tuple
    returns True if comb_sum and comb have same number of non-zero digits
    """
    num_of_nonzero_digits = len([i for i in str(comb_sum) if i != '0'])
    j = 0
    while comb[j] == 0:
        j += 1
    if num_of_nonzero_digits == len(comb[j:]):
        return True
    else:
        return False


def digit_Nth_powers(power):
    m = find_max_number_of_digits(power)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = []
    for comb in combinations_with_replacement(digits, m):
        if sum(comb) == 1:
            continue
        if sum(comb) == 0:
            continue
        comb_sum = sum_power(power, comb)
        if not same_number_of_digits(comb_sum, comb):
            continue
        digits_of_sum = Counter([int(i) for i in str(comb_sum)])
        digits_of_comb = Counter(comb)
        found_num = True
        for digit in digits_of_sum:
            if digit not in digits_of_comb or digits_of_sum[digit] > digits_of_comb[digit]:
                found_num = False
        if found_num:
            numbers.append(comb_sum)
    return sum(numbers)


if __name__ == '__main__':
    print(digit_Nth_powers(int(input())))
