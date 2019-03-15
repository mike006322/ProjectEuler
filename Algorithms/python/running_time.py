from time import time


def running_time(f):
    # decorator adds running time as a function variable
    def new_f(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        elapsed = end - start
        new_f.running_time = str(elapsed) + ' seconds have elapsed for ' + str(f.__name__) + '(' + str(*args) + str(**kwargs) + ')'
        return res
    return new_f


def get_div_sum(n):
    res = 0
    for i in range(2, int(n**.5) + 1):
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
    from Algorithms.python.Sieve_of_Eratosthenes import Sieve_of_Eratosthenes_numpy

    Sieve_of_Eratosthenes_numpy = running_time(Sieve_of_Eratosthenes_numpy)
    Sieve_of_Eratosthenes_numpy(6000000)
    print(Sieve_of_Eratosthenes_numpy.running_time)

    # primes = Sieve_of_Eratosthenes_numpy(1000000000)
    # primesset = set(primes)
    # print(primes[-1])
    # time_function(get_div_sum, [1000000000])
    # time_function(fast_sum_of_proper_divisors, (999999937, primes, primesset))

