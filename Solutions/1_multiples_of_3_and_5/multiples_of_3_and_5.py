#!/bin/python3

#https://www.hackerrank.com/contests/projecteuler/challenges/euler001

def multiples_of_3_and_5(n):
    """
    input integer n
    return sum of multiples of 3 and 5 below n
    """
    num_mul_3 = (n-1)//3
    num_mul_5 = (n-1)//5
    num_mul_15 = (n-1)//15
    sum_mul_3 = 3*num_mul_3*(num_mul_3 + 1)//2
    sum_mul_5 = 5*num_mul_5*(num_mul_5 + 1)//2
    sum_mul_15 = 15*num_mul_15*(num_mul_15 + 1)//2
    res = sum_mul_3 + sum_mul_5 - sum_mul_15
    return res


if __name__ == '__main__':
    print(multiples_of_3_and_5(1000))
    # t = int(input().strip())
    # for a0 in range(t):
    #     n = int(input().strip())
    #     num_mul_3 = (n-1)//3
    #     num_mul_5 = (n-1)//5
    #     num_mul_15 = (n-1)//15
    #     sum_mul_3 = 3*num_mul_3*(num_mul_3 + 1)//2
    #     sum_mul_5 = 5*num_mul_5*(num_mul_5 + 1)//2
    #     sum_mul_15 = 15*num_mul_15*(num_mul_15 + 1)//2
    #     res = sum_mul_3 + sum_mul_5 - sum_mul_15
    #     print(res)
