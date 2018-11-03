#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

# formula for sum of numbers: https://brilliant.org/wiki/sum-of-n-n2-or-n3/


def sum_1_to(n):
    return n*(n+1)//2


def multiples_of_3_and_5(n):
    """
    return sum of multiples of 3 and 5 below n
    """
    number_of_multiples_of_3 = (n-1)//3
    number_of_multiples_of_5 = (n-1)//5
    number_of_multiples_of_15 = (n-1)//15
    sum_of_multiples_of_3 = 3*sum_1_to(number_of_multiples_of_3)
    sum_of_multiples_of_5 = 5*sum_1_to(number_of_multiples_of_5)
    sum_of_multiples_of_15 = 15*sum_1_to(number_of_multiples_of_15)
    return sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15


if __name__ == '__main__':
    # print(multiples_of_3_and_5(1000))
    pass
