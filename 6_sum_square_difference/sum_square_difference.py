#https://www.hackerrank.com/contests/projecteuler/challenges/euler006

def sum_square_difference(n):
    return (n**2)*((n+1)**2)//4 - n*(n+1)*(2*n+1)//6

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sum_square_difference(n))
