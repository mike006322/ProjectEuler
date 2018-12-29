#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler040

# 1 - 9 (9 numbers, 9 digits, begins i_1, ends i_9)
# 10 - 99 (90 numbers, 90*2 digits, begins i_10, ends i_10+90*2 - 1 = i_189)
# 100 - 999 (900 numbers, 900*3 digits)
# 1000 - 9999 (9000)
# 10000 - 99999 (90000)
# store this table up to 10^18th
#
# store for each grouping begin, end, number of digits


def make_lookup_table(n):
    """
    n is the max number of digits the table goes to
    """
    lookop_table = list()
    digit_number = 0
    for i in range(1, n+1):
        begin = digit_number + 1
        end = digit_number + 9*i*10**(i-1)
        digit_number = end
        lookop_table.append((begin, end))
        # index of the lookuptable + 1 is the number of digits of the number
    return lookop_table


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


def find_d_i_n(n, lookup_table):
    """
    input: digit number n
    output: what the digit is
    """
    # print('n = ', n)
    # find the number of digits of the number, z, that i_n is in via lookup table
    i = 0
    while True:
        if lookup_table[i][0] <= n <= lookup_table[i][1]:
            i += 1
            break
        i += 1
    if i == 1:
        return n
    # subtract the number of digits from Champerowne's constant that represent fewer digits than z, call this m
    # print('i = ', i)
    m = n - lookup_table[i-1][0] + 1
    # print('m = ', m)
    # divide m by number of digits of z to get the rth number that is of that many digits
    r = m // i
    if m % i != 0:
        r += 1
    # print('r = ', r)
    # mod m by number of digits of z to get the digit within that number representing i_n
    j = (m-1) % i
    # print('j = ', j)
    return make_digits(10**(i-1) + r - 1)[j]


if __name__ == '__main__':
    lookup_table = make_lookup_table(18)
    t = int(input())
    for _ in range(t):
        digits = map(int, input().split())
        product = 1
        for digit in digits:
            product *= find_d_i_n(digit, lookup_table)
        print(product)
