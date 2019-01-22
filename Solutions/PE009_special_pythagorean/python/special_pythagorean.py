#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler009


def generate_primitive_pythagorean_triples(N):
    """
    generates all primitive pythagorean triples such that a + b + c <= n
    """
    res = []
    n = 1
    while n < N//3 + 1:
        m = n + 1
        while 2*m*n + 2*m**2 <= N:
            res.append({2*m*n, (m**2 - n**2), m**2 + n**2})
            m += 1
        n += 1
    return res


def check_multiples_of_primitives(primitives, N):
    """
    for each triple in the list of primitives it finds all multiples such that k(a + b + c) = n
    returns a set of the triples
    """
    res = set()
    for triple in primitives:
        i = 1
        while i*sum(triple) <= N:
            if i*sum(triple) == N:
                triple = list(triple)
                res.add((i*triple[0], i*triple[1], i*triple[2]))
            i += 1
    return res


def choose_largest(triples):
    """
    returns the largest product of a triple
    """
    if len(triples) == 0:
        return -1
    m = 0
    for triple in triples:
        product = triple[0]*triple[1]*triple[2]
        if product > m:
            m = product
    return m


def special_pythagorean(N):
    if N % 2 != 0:
        return -1
    primitives = generate_primitive_pythagorean_triples(N)
    triples = check_multiples_of_primitives(primitives, N)
    m = choose_largest(triples)
    return m


if __name__ == '__main__':
    # primitives = generate_primitive_pythagorean_triples(1000)
    # print(list(check_multiples_of_primitives(primitives, 1000))[-1])
    # print(generate_primitive_pythagorean_triples(130))
    # print(11*60*61)
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(special_pythagorean(n))
