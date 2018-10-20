#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler027

def Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]

def how_many_primes(a, b, primes):
    """
    input are two integers, a and b
    output the number of consecutive primes the formula n^2+an+b generates, where n starts with 0
    """
    res = 0
    while res**2 + a*res + b in primes:
        res += 1
    return res + 1


def quadratic_primes(N):
    """
    input N >= 42
    output a list of coefficients(a, b) to n^2+an+b that produce the most consecutive primes where abs(a), abs(b) <= N
    for each number 42 to N
    """
    primes = set(Sieve_of_Eratosthenes(4000))
    res = [0]*(N+1)
    max_primes = 42
    res[42] = (-1, 41)
    max_a, max_b = -1, 41
    for i in range(43, N+1):
        for a in range(-i, i+1):
            num_primes = how_many_primes(a, i, primes)
            if num_primes > max_primes:
                max_primes = num_primes
                max_a, max_b = a, i
        for b in range(-i, i+1):
            num_primes = how_many_primes(i, b, primes)
            if num_primes > max_primes:
                max_primes = num_primes
                max_a, max_b = i, b
        res[i] = (max_a, max_b)
    return res


if __name__ == '__main__':
    N = 1000
    res = quadratic_primes(N)
    print(*res[N])
