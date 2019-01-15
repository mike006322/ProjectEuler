#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler047


def Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]


def distinct_prime_factors(N, K):
    primes = Sieve_of_Eratosthenes(int(N/K) + 1)
    nums = [0]*(N+K+1)
    for p in primes:
        i = 1
        while i*p <= N+K:
            nums[i*p] += 1
            i += 1
    for i in range(1, N + 1):
        if nums[i] == K:
            consecutive = True
            j = 1
            while j < K:
                if nums[i + j] != K:
                    consecutive = False
                    break
                j += 1
            if consecutive:
                print(i)


if __name__ == '__main__':
    distinct_prime_factors(*map(int, input().split()))
