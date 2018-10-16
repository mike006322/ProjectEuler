#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler023

# Every integer greater than 20161 can be written as the sum of two abundant numbers
# find abundant numbers up to 20161
# find the sums of pairs of abundant numbers


def Sieve_of_Eratosthenes(n):
    """
    Return list of primes less than n
    """
    res = [2]
    i = 3
    marked = set()
    while i <= n**.5:
        if i not in marked:
            res.append(i)
            j = 0
            while j <= n/i:
                marked.add(i + j*i)
                j += 1
        i += 2
    while i <= n:
        if i not in marked:
            res.append(i)
        i += 2
    return res

def sum_of_proper_divisors(n, primes):
    """
    input n and a list of primes
    returns the sum of the proper divisors
    """
    b = n
    product = 1
    for p in primes:
        if p > n:
            break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i != 0:
            product *= (p**(i + 1) - 1)//(p - 1)
    return product - b

def find_abundant_numbers():
    """
    finds abundant numbers up to 20161
    """
    res = set()
    primes = Sieve_of_Eratosthenes(20161//2)
    for i in range(12, 20162):
        if i not in res:
            if sum_of_proper_divisors(i, primes) > i:
                j = 1
                while j*i <= 20161:
                    res.add(j*i)
                    j += 1
    return res

if __name__ == '__main__':
    abundant_numbers = find_abundant_numbers()
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n > 20161:
            print('YES')
        else:
            can_sum = False
            for a in abundant_numbers:
                if n - a in abundant_numbers:
                    print('YES')
                    can_sum = True
                    break
            if not can_sum:
                print('NO')
