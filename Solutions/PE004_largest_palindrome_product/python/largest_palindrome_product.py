#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler004


def next_palindrome(n):
    """
    101101 < n < 1000000
    takes n and returns the next palindrome number counting down
    """
    str_n = str(n)
    first_half = int(str_n[:3])
    first_half -= 1
    first_half = str(first_half)
    res = first_half + first_half[2] + first_half[1] + first_half[0]
    return int(res)


def has_three_digit_factors(n):
    """
    incrimints from 101 to 999 looking for 3 digit factors
    if a 3 digit factor is found then checks if the other factor is 3 digit or moves on
    """
    i = 100
    while i < 1000:
        if n % i == 0:
            d = n//i
            if 99 < d < 1000:
                return True
        i += 1
    return False


def largest_palindrome_product(n):
    """
    first check if n in palindrome
    if n is a palindrome, run try_three_digits on it
    then change n with next_palindrome and keep running try_three_digits
    if n is not a palindrome then go right to find_next_palindrome
    """
    n -= 1
    while str(n)[:3] != str(n)[5] + str(n)[4] + str(n)[3]:
            n -= 1
    while not has_three_digit_factors(n):
        n = next_palindrome(n)
    return n


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(largest_palindrome_product(n))

