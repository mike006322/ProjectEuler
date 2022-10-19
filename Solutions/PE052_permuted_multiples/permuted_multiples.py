# https://www.hackerrank.com/contests/projecteuler/challenges/euler052/problem

from collections import Counter


def permuted_multiples(N: int, K: int):
    for x in range(1, N + 1):
        digits = Counter(str(x))
        for k in range(2, K+1):
            if Counter(str(k * x)) != digits:
                break
        else:
            res = ''
            for k in range(1, K+1):
                res +=  str(k*x) + " "
            yield res

def main():
    N, K = input().split()
    for s in permuted_multiples(int(N), int(K)):
        print(s)


if __name__ == '__main__':
    main()
