#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler028

"""
https://math.stackexchange.com/questions/1347560/quadratic-polynomials-describe-the-diagonal-lines-in-the-ulam-spiral

Equations for diagonals:
4*n**2 - 2*n + 1
4*(n+1)**2 - 4*(n+1) + 1 = 4*n**2 + 4*n + 1
4*n**2 + 2*n + 1
4*n**2 + 1

sum_1_to_n(4*n**2 - 2*n + 1) = 4*sum_1_to_n(n**2) - 2*sum_1_to_n(n) + sum_1_to_n(1)
formula for sum of squares: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
sum_1_to_n(i**2): (n*(n + 1)*(2n + 1))//6
sum_1_to_n(i): n*(n+1)//2

in an NxN square there are N//2 = (N-1)/2 entries on each diagonal.
The sum is all of the diagonals plus the middle 1

sum_of_all_diagonals = sum_1_to_N//2(4*i**2 - 2*i + 1 + 4*i**2 + 4*i + 1 + 4*i**2 + 2*i + 1 + 4*i**2 + 1) + 1
= sum_1_to_N//2(16*i**2 + 4*i + 4) + 1
= 16*sum_1_to_N//2(i**2) + 4*sum_1_to_N//2(i) + 4*sum_1_to_N//2(1) + 1
= 16*(N-1)*(N+1)*N/24 + 4*(N-1)(N+1)/8 + 4*(N-1)/2 + 1
= 2*(N-1)*(N+1)*N/3 + (N-1)(N+1)/2 + 2*(N-1) + 1
= 2*(N-1)*(N+1)*N/3 + (N-1)(N+1)/2 + 2*N - 1
"""

def number_spiral_diagonals(n):
    mod = 1000000007
    return ((2*(n-1)*(n+1)*n)//3 + ((n-1)*(n+1))//2 + 2*n - 1) % mod


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(number_spiral_diagonals(int(input())))
