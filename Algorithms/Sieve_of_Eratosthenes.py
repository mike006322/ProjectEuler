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
            while j <= n:
                marked.add(i + j)
                j += i
        i += 2
    while i <= n:
        if i not in marked:
            res.append(i)
        i += 2
    return res

def fast_Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]

import numpy

def Sieve_of_Eratosthenes_numpy(n):
    """
    Returns a list of primes to n
    """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return [2] + list(2*numpy.nonzero(sieve)[0][1::] + 1)

if __name__ == '__main__':
    assert Sieve_of_Eratosthenes_numpy(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert fast_Sieve_of_Eratosthenes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert Sieve_of_Eratosthenes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert Sieve_of_Eratosthenes_numpy(105000)[10000] == 104743
