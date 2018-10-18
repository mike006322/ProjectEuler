#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler018

# maintain a list that iterates over the number of rows that lists the maximum lengths to the position
# make it equal to first row first

def max_path_sum(a):
    """
    input is list of lists that make pyramid
    output is int representing max length sum
    """
    b = a[0]
    n = len(a)
    for i in range(1, n):
        c = []
        c.append(a[i][0]+b[0])
        for j in range(1, i):
            c.append(max(a[i][j] + b[j], a[i][j] + b[j-1]))
        c.append(a[i][i] + b[i-1])
        b = c
    return max(b)

if __name__ == '__main__':
    file = open('numbers.txt', 'r')
    a = []
    for line in file:
        b = list(map(int, line.split()))
        a.append(b)
    print(max_path_sum(a))
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     a = []
    #     for i in range(n):
    #         b = list(map(int, input().split()))
    #         a.append(b)
    #     print(max_path_sum(a))
