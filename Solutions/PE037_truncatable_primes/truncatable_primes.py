#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler037


def has_digits(n, digits):
    """
    returns boolean whether digits are in n
    """
    res = False
    for digit in make_digits(n):
        if digit in digits:
            return True
    return False


def Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]


def make_digits(n):
    """
    input integer
    output tuple of digits of integer (base 10)
    """
    return tuple(int(x) for x in str(n))


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


def remove_digit(n, side):
    if type(n) == tuple:
        digits = list(n)
    else:
        digits = n
    if side == 'left':
        digits.pop(0)
        return digits
    if side == 'right':
        digits.pop()
        return digits


def truncatable_primes(n):
    res = set()
    primes = Sieve_of_Eratosthenes(n)
    check_primes = set(primes)
    for p in primes:
        is_tp = True
        p_left = make_digits(p)
        while len(p_left) > 1:
            p_left = remove_digit(p_left, 'left')
            if make_number(p_left) not in check_primes:
                is_tp = False
                break
        if not is_tp:
            continue
        p_right = make_digits(p)
        while len(p_right) > 1:
            p_right = remove_digit(p_right, 'right')
            if make_number(p_right) not in check_primes:
                is_tp = False
                break
        if is_tp:
            res.add(p)
    return sum(res) - 17


if __name__ == '__main__':
    n = int(input())
    print(truncatable_primes(n))
