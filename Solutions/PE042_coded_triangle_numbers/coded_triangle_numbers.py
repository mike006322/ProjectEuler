#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler042

# .5(n^2 + n) = int(input()) = m
# -.5 +- (.25 + 2*m)**.5


def coded_triangle_numbers(n):
    res = -.5 + (.25 + 2*n)**.5
    if int(res) == res:
        return int(res)
    else:
        return -1


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     print(coded_triangle_numbers(int(input())))

    filename = "p042_words.txt"
    file = open(filename, "r")
    triangle_words = 0
    for line in file:
        for word in line.replace('"','').split(","):
            value = 0
            for letter in word:
                value += ord(letter) - 64
            c = coded_triangle_numbers(value)
            if c != -1:
                triangle_words += 1
    print(triangle_words)
