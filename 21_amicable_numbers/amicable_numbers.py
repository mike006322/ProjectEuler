#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler021

from itertools import combinations

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

def divisors(n):
    """
    returns a list of all the divisors of n that are less than n
    """
    primes = Sieve_of_Eratosthenes(n)
    single_prime_divisors = []
    for p in primes:
        i = 1
        while n % p**i == 0 and p**i != n:
            single_prime_divisors.append(p**i)
            i += 1
    res = [1] + single_prime_divisors[:]
    for i in range(2, len(single_prime_divisors)+1):
        for t in combinations(single_prime_divisors, i):
            product = 1
            for num in t:
                product *= num
            if product < n and n % product == 0:
                res.append(product)
    return res

def d(n):
    return sum(divisors(n))

def amicable_numbers(N):
    """
    return the sum of all amicable number pairs less than N
    """
    if N < 220:
        return 0
    res = []
    an = dict()
    i = 220
    check = []
    while i <= N:
        di = d(i)
        if di > N:
            an[i] = di
            if i == d(di):
                res.append(i)
            i += 1
        elif 219 < di <= i:
            if an[di] == i:
                res.append(di + i)
            i += 1
        else:
            an[i] = di
            check.append((i, di))
            i += 1
    return sum(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(amicable_numbers(N))
