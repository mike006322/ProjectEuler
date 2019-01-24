#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler046

from Algorithms.python.Sieve_of_Eratosthenes import fast_Sieve_of_Eratosthenes as Sieve_of_Eratosthenes


def is_square(n):
    """
    return boolean whether n is a square
    """
    if n**.5 % 1 == 0:
        return True
    else:
        return False


def goldbachs_other_conjecture(n, primes):
    """
    input odd composite number n and a list of primes
    returns the number of ways n can be written as a sum of a prime and twice a square
    """
    res = 0
    for p in primes:
        if p < n:
            m = n
            m -= p
            m /= 2
            if is_square(m):
                res += 1
        else:
            break
    return res


if __name__ == '__main__':
    # t = int(input())
    primes = Sieve_of_Eratosthenes(5*10**5)
    # for _ in range(t):
    #     print(goldbachs_other_conjecture(int(input()), primes))
    for i in range(3, 10**6, 2):
        if i not in primes:
            if goldbachs_other_conjecture(i, primes) == 0:
                print(i)
                break
