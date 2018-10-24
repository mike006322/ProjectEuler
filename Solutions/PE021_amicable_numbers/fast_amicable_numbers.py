#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler021

def Sieve_of_Eratosthenes(n):
    """
    Return list of primes less than n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]

def Sieve_of_Eratosthenes_TF_List(n):
    """
    Return list of primes less than n
    """
    res = [False]*(n+1)
    res[2] = True
    i = 3
    marked = set()
    while i <= n**.5:
        if i not in marked:
            res[i] = True
            j = 0
            while j <= n:
                marked.add(i + j)
                j += i
        i += 2
    while i <= n:
        if i not in marked and i % 2 != 0:
            res[i] = True
        i += 1
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

def fast_sum_of_proper_divisors(n, primes, is_prime):
    """
    input n and a list of primes
    returns the sum of the proper divisors
    """
    if is_prime[n]:
        return 1
    n_copy = n
    product = 1
    for p in primes:
        if is_prime[n]:
            product *= (n**(1 + 1) - 1)//(n - 1)
            break
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
    is_prime = Sieve_of_Eratosthenes_TF_List(int(N*1.4))
    res = set()
    d = [0]*10000000
    for i in range(220, N+1):
        d[i] = fast_sum_of_proper_divisors(i, primes, is_prime)
        if 1.4*i > d[i] > N:
            if d[d[i]] == 0:
                if i != d[i]:
                    d[d[i]] = fast_sum_of_proper_divisors(d[i], primes, is_prime)
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
    # a = amicable_numbers(10000)
    # print(sum(a))
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
