#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler035


def rotations(a):
    """
    yields rotations of the iterable a
    """
    a = list(a)
    r = 0
    n = len(a)
    res = set()
    while r < n:
        res.add(tuple(a))
        r += 1
        b = a.pop(0)
        a.append(b)
    return res


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


def has_digits(n, digits):
    """
    returns boolean whether digits are in n
    """
    res = False
    for digit in make_digits(n):
        if digit in digits:
            return True
    return False


def Sieve_of_Eratosthenes_without_0_2_4_5_6_8(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2, 3, 5] + [2*i + 1 for i in range(1, n//2) if sieve[i] and not has_digits(2*i + 1, {0, 2, 4, 5, 6, 8})]


def circular_primes(n):
    """
    returns the sum of all circular primes less than n
    """
    res = set()
    n_digits = make_digits(n)
    max_n = make_number([9]*len(n_digits))
    primes = Sieve_of_Eratosthenes_without_0_2_4_5_6_8(max_n + 1)
    checked = set()
    for p in primes:
        if p in checked:
            continue
        if p >= n:
            break
        is_circular = True
        p_digits = make_digits(p)
        p_total = set()
        for num_digits in rotations(p_digits):
            num = make_number(num_digits)
            checked.add(num)
            if num not in primes:
                is_circular = False
            else:
                if num < n:
                    p_total.add(num)
        if is_circular:
            res = res.union(p_total)
    return sum(res)


if __name__ == '__main__':
    n = int(input())
    print(circular_primes(n))
