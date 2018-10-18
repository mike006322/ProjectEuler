#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler012

def count_divisors(n):
    """
    input integer n
    returns the number of divisors of n
    """
    res = 0
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            # If divisors are equal, count only one
            if n/i == i:
                res += 1
            # Otherwise count both
            else:
                res += 2
    return res

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

def fast_count_divisors(n, primes):
    """
    counts divisors using a table of primes
    """
    # primes = Sieve_of_Eratosthenes(1000000)
    i = 0
    divisors = 1
    while primes[i] <= n:
        p = primes[i]
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            divisors *= count + 1
        i += 1
    return divisors

def triangle_number_with_n_divisors(n):
    i = 1
    triangle = 1
    divisors = 1
    while divisors <= n:
        i += 1
        triangle += i
        divisors = count_divisors(triangle)
        #print(i, triangle, divisors)
    return triangle

def triangle_number_with_more_than_n_divisors(n):
    i = 1
    triangle = 1
    divisors = 1
    m = 1
    table = dict()
    table[0] = triangle
    primes = Sieve_of_Eratosthenes(1000000)
    while divisors <= n:
        i += 1
        triangle += i
        divisors = fast_count_divisors(triangle, primes)
        if divisors > m:
            for j in range(m, divisors):
                table[j] = triangle
            m = divisors
    return table

if __name__ == '__main__':
    table = triangle_number_with_more_than_n_divisors(500)
    print(table[500])
    # table = triangle_number_with_more_than_n_divisors(1000)
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     print(table[n])
