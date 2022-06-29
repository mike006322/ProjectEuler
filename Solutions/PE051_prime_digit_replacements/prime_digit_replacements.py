#  https://www.hackerrank.com/contests/projecteuler/challenges/euler051/problem
import itertools
import time
from collections import defaultdict


def timer_func(func):
    def wrap_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__!r} executed in {(end - start):.4f}s')
        return result

    return wrap_func


def make_9_number(m):
    """
    returns int of n 9's
    e.g.: n = 3, return 999
    """
    if m == 0:
        return 0
    res = ''
    for _ in range(m):
        res += '9'
    return int(res)


def find_primes_of_n_digits(n: int) -> list:
    """
    returns list of all primes with n digits
    """
    small_nines = make_9_number(n - 1)
    big_nines = make_9_number(n)
    sieve = [True] * (big_nines // 2)
    for i in range(3, int(big_nines ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((big_nines - i * i - 1) // (2 * i) + 1)
    if 2 > small_nines:
        return [2] + [2 * i + 1 for i in range(1, big_nines // 2) if sieve[i] and small_nines < 2 * i + 1 < big_nines]
    else:
        return [2 * i + 1 for i in range(1, big_nines // 2) if sieve[i] and small_nines < 2 * i + 1 < big_nines]


def numbers_with_k_repeated_digits(n: int, k: int) -> list:
    """
    :param n:
    :param k:
    If n has k repeated digits, for each set of k,
    add to list (n, s) where is is a string that is n without k repeated digits
    :return:
    """
    res = []
    str_n = str(n)
    seen = set()
    for i in str_n:
        if i in seen:
            continue
        seen.add(i)
        count = str_n.count(i)
        if count == k:
            res.append((str_n.replace(i, 'X'), n))
        if count > k:
            # Indexes of digits in n
            all_indexes = [j for j, c in enumerate(str_n) if c == i]
            # choose k
            for indexes in itertools.combinations(all_indexes, k):
                new_n = str_n
                for index in indexes:
                    new_n = new_n[:index] + 'X' + new_n[index + 1:]
                res.append((new_n, n))
    return res


@timer_func
def test2():
    start_time = time.time()
    N, K, L = 2, 1, 3
    prime_digit_replacement(N, K, L)


@timer_func
def test3():
    N, K, L = 5, 2, 7
    prime_digit_replacement(N, K, L)


@timer_func
def test4():
    N, K, L = 7, 1, 7
    prime_digit_replacement(N, K, L)


def apply_mask(n: str, mask: tuple) -> str:
    """
    :param n: number
    :param mask: indexes of digits to replace
    :return: digits with 'X's where mask is
    """
    for index in mask:
        n = n[:index] + 'X' + n[index + 1:]
    return n


def digits_same(n: str, mask: tuple):
    first_digit = n[mask[0]]
    for index in mask[1:]:
        if n[index] != first_digit:
            return False
    return True


def prime_digit_replacement(N: int, K: int, L: int):
    if K == 1:
        prime_digit_replacement_K_1(N, L)
        return
    sequences = []
    templates = defaultdict(list)
    # {template_string: value_list}
    # e.g. {'56xx3': [56003]}
    for prime in find_primes_of_n_digits(N):
        for template, value in numbers_with_k_repeated_digits(prime, K):
            templates[template].append(value)
    for template in templates:
        if len(templates[template]) >= L:
            sequences.append(tuple(templates[template][:L]))
    print(*min(sequences))


def prime_digit_replacement_K_1(N: int, L: int):
    sequences = []
    templates = defaultdict(dict)
    # {template_string: {digit: value}}
    # e.g. {'56xx3': {0: 56003}}}
    n_digit_primes = find_primes_of_n_digits(N)
    for mask in range(N):
        for prime in n_digit_primes:
            str_prime = str(prime)
            masked = apply_mask(str_prime, (mask,))
            if mask not in templates[masked]:
                templates[masked][str_prime[mask]] = prime
        for template in templates:
            if len(templates[template]) >= L:
                sequences.append(tuple(templates[template].values())[:L])
        templates = defaultdict(dict)
    print(*min(sequences))


if __name__ == '__main__':
    # N, K, L = map(int, input().split())
    # prime_digit_replacement(N, K, L)
    test4()
