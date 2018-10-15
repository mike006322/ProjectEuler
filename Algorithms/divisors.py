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

def prime_factorization(n):
    """
    returns a list of tuples (p, power_of_p)
    """
    primes = Sieve_of_Eratosthenes(n)
    res = []
    for p in primes:
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            res.append((p, i))
    return res

# https://en.wikipedia.org/wiki/Divisor_function

def sum_of_divisors(n):
    """
    returns the sum of divisors of n
    """
    product = 1
    for p, power in prime_factorization(n):
        product *= (p**(power + 1) - 1)//(p - 1)
    return product

def sum_of_proper_divisors(n):
    """
    returns the sum of proper divisors of n
    """
    product = 1
    for p, power in prime_factorization(n):
        product *= (p**(power + 1) - 1)//(p - 1)
    return product - n

def sum_of_proper_divisors2(n, primes):
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


if __name__ == '__main__':
    assert divisors(3) == [1]
    assert divisors(10) == [1, 2, 5]
    assert divisors(8) == [1, 2, 4]
    assert divisors(220) == [1, 2, 4, 5, 11, 10, 22, 20, 44, 55, 110]
    assert prime_factorization(4) == [(2, 2)]
    assert prime_factorization(10) == [(2, 1), (5, 1)]
    assert prime_factorization(100) == [(2, 2), (5, 2)]
    a = []
    for j in range(1, 14):
        a.append(sum_of_divisors(j))
    assert a == [1, 3, 4, 7, 6, 12, 8, 15, 13, 18, 12, 28, 14]
    assert sum_of_proper_divisors(4) == 3
    primes = Sieve_of_Eratosthenes(100)
    assert sum_of_proper_divisors2(8, primes) == sum_of_proper_divisors(8)
    assert sum_of_proper_divisors2(100, primes) == sum_of_proper_divisors(100)
    assert sum_of_proper_divisors2(220, primes) == sum_of_proper_divisors(220)
