#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler013

def large_sum(nums):
    res = ''
    n = sum(nums)
    for i in range(10):
        res += str(n)[i]
    return res

if __name__ == '__main__':
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(large_sum(nums))
