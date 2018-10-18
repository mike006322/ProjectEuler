#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler021

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
    n_copy = n
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
    return product - n_copy


def amicable_numbers(N):
    """
    return a set of all amicable numbers less than N
    """
    primes = Sieve_of_Eratosthenes(N)
    res = set()
    d = [0]*10000000
    for i in range(220, N+1):
        d[i] = sum_of_proper_divisors(i, primes)
        if 1.4*i > d[i] > N:
            if d[d[i]] == 0:
                if i != d[i]:
                    d[d[i]] = sum_of_proper_divisors(d[i], primes)
                    if i == d[d[i]]:
                        res.add(i)
            else:
                if i == d[d[i]]:
                        res.add(i)
        elif d[i] < i:
            if i == d[d[i]]:
                res.add(i)
                res.add(d[i])
    return res


if __name__ == '__main__':
    # print(amicable_numbers(1000))
    t = int(input())
    Ns = []
    max_N = 0
    for _ in range(t):
        num = int(input())
        Ns.append(num)
        if num > max_N:
            max_N = num
    a = amicable_numbers(max_N)
    for N in Ns:
        res = 0
        for num in a:
            if num <= N:
                res += num
        print(res)
