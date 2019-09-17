#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler049/problem


def fast_Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    modified to make them all have the same number of digits
    """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def prime_permutations(N, K):
    """
    input N, K
    find all K size sequences, where first element is less than N
    elements are permutations, prime, arithmetic progression
    """
    # make primes_of_same_stringlength
    # make hash table H = {prime, sorted_prime}
    # H.items() sorted by sorted prime
    # look for K_many together

    res = []

    primes_of_same_stringlength = fast_Sieve_of_Eratosthenes(10 ** len(str(N)))
    primes_with_sorted_strings = dict()
    for prime in primes_of_same_stringlength:
        if tuple(sorted(str(prime))) in primes_with_sorted_strings:
            primes_with_sorted_strings[tuple(sorted(str(prime)))].append(prime)
        else:
            primes_with_sorted_strings[tuple(sorted(str(prime)))] = [prime]
    for string in primes_with_sorted_strings:
        if len(primes_with_sorted_strings[string]) >= K:
            for i, first_prime in enumerate(primes_with_sorted_strings[string]):
                if first_prime <= N:
                    if K == 3:
                        for j in range(i+1, len(primes_with_sorted_strings[string])):
                            middle = (primes_with_sorted_strings[string][j] - first_prime) // 2 + first_prime
                            if middle in primes_with_sorted_strings[string]:
                                s = str(first_prime) + str(middle) + str(primes_with_sorted_strings[string][j])
                                res.append(int(s))
                    if K == 4:
                        for j in range(i+1, len(primes_with_sorted_strings[string])):
                            difference = (primes_with_sorted_strings[string][j] - first_prime) // 3
                            middle_1 = difference + first_prime
                            if middle_1 in primes_with_sorted_strings[string]:
                                middle_2 = difference*2 + first_prime
                                if middle_2 in primes_with_sorted_strings[string]:
                                    s = str(first_prime) + str(middle_1) + str(middle_2) + str(primes_with_sorted_strings[string][j])
                                    res.append(int(s))
    for item in sorted(res):
        print(item)


if __name__ == '__main__':
    prime_permutations(3000, 3)
    # prime_permutations(*map(int, input().split()))
