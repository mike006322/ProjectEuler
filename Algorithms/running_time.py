from time import time

def time_function(f, i):
    """
    returns the time it takes to run function f with input i
    """
    start = time()
    f(*i)
    end = time()
    elapsed = end - start
    print(elapsed, ' seconds have elapsed for ', f,)# ' with input ', i)
    return elapsed

import math

def getDivSum(n):
    res = 0
    for i in range(2, (int)(math.sqrt(n))+1):
        if n % i == 0:
            if i == (n / i):
                res += i
            else:
                res += i + n / i
    res += 1
    return int(res)

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

def fast_sum_of_proper_divisors(n, primes, primesset):
    """
    input n and a list of primes
    returns the sum of the proper divisors
    """
    if n in primesset:
        return 1
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



if __name__ == '__main__':

    from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes
    from Sieve_of_Eratosthenes import fast_Sieve_of_Eratosthenes
    from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes_numpy

    # time_function(Sieve_of_Eratosthenes, 1000000)
    # time_function(fast_Sieve_of_Eratosthenes, 1000000)
    # time_function(Sieve_of_Eratosthenes_numpy, 1000000)

    primes = Sieve_of_Eratosthenes_numpy(1000000000)
    primesset = set(primes)
    print(primes[-1])
    time_function(getDivSum, [1000000000])
    time_function(fast_sum_of_proper_divisors, (999999937, primes, primesset))

