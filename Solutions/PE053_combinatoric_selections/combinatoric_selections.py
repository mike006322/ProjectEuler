# https://www.hackerrank.com/contests/projecteuler/challenges/euler053/problem?isFullScreen=true

from math import prod


def n_choose_r(n: int, r: int):
    return prod(range(r + 1, n + 1)) // prod(range(1, n - r + 1))


def combinatoric_selections(N: int, K: int):
    total_combos = 0
    for n in range(1, N + 1):
        # use symmetry: nCr = nC(n-r)
        has_some_above_K = False
        r = 1
        while r <= n//2:
            if n_choose_r(n, r) > K:
                has_some_above_K = True
                break
            r += 1
        if has_some_above_K:
            if n % 2 == 0:
                total_combos += n - 2*(r-1) - 1
            else:
                total_combos += 2*(n//2 - (r - 1))
    return total_combos


def main():
    N, K = input().split()
    print(combinatoric_selections(int(N), int(K)))


if __name__ == '__main__':
    main()
