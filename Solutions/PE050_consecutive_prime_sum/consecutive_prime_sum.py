# https://www.hackerrank.com/contests/projecteuler/challenges/euler050/problem


def Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


PRIMES_UNDER_10_MIL = Sieve_of_Eratosthenes(10000000)
PRIMES_UNDER_10_MIL_SET = set(PRIMES_UNDER_10_MIL)


def is_prime(n):
    """
    Returns boolean whether n is prime
    """
    if n < 10000000:
        return n in PRIMES_UNDER_10_MIL_SET
    i = 0
    root_n = n ** .5
    while PRIMES_UNDER_10_MIL[i] <= root_n:
        if n % PRIMES_UNDER_10_MIL[i] == 0:
            return False
        i += 1
    return True


def find_max_consecutive_prime_sum_indexed_at_0(n):
    """
    finds the max prime that is a sum of primes starting at first prime (index 0)
    """
    # start from the back
    # get odd prime sum closest to n
    prime_sum = 0
    i = 0
    while prime_sum <= n:
        prime_sum += PRIMES_UNDER_10_MIL[i]
        i += 1
    i -= 1
    prime_sum -= PRIMES_UNDER_10_MIL[i]
    if prime_sum % 2 == 0:
        i -= 1
        prime_sum -= PRIMES_UNDER_10_MIL[i]

    while prime_sum <= n:
        if is_prime(prime_sum):
            return prime_sum, i
        prime_sum -= PRIMES_UNDER_10_MIL[i - 1]
        prime_sum -= PRIMES_UNDER_10_MIL[i - 2]
        i -= 2


def find_max_consecutive_prime_sum_indexed_at_k(progress, progress_index, num_consecutive, k, n):
    """
    input 'progress' which is a sum of PRIME_NUMBERS_UNDER_10_MIL[progress_index: progress_index + num_consecutive]
    Look for sums with more than num_consecutive summands starting at index k
    """
    max_progress = 0
    max_num_consecutive = 0
    for i in range(k - progress_index):
        progress -= PRIMES_UNDER_10_MIL[progress_index + i]
        progress += PRIMES_UNDER_10_MIL[progress_index + num_consecutive + i]
    halt = True
    while progress <= n:
        halt = False
        progress += PRIMES_UNDER_10_MIL[k + num_consecutive]
        num_consecutive += 1
        if progress <= n:
            if is_prime(progress):
                max_progress = progress
                max_num_consecutive = num_consecutive
    return max_progress, k, max_num_consecutive, halt


def find_max_consecutive_prime_sum(n):
    if n < 5:
        return 2, 1
    progress, num_consecutive = find_max_consecutive_prime_sum_indexed_at_0(n)
    progress_index = 0
    halt = False
    k = 1
    while not halt:
        check_progress, check_index, check_consecutive, halt = find_max_consecutive_prime_sum_indexed_at_k(progress,
                                                                                                           progress_index,
                                                                                                           num_consecutive,
                                                                                                           k, n)
        if check_progress != 0:
            progress = check_progress
            progress_index = check_index
            num_consecutive = check_consecutive
        k += 1
    return progress, num_consecutive


if __name__ == '__main__':
    print(find_max_consecutive_prime_sum_indexed_at_0(1000))
    print(find_max_consecutive_prime_sum(1000000000000))
    # for _ in range(int(input())):
    #     n = int(input())
    #     print(*find_max_consecutive_prime_sum(n))
