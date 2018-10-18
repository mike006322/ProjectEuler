#https://www.hackerrank.com/contests/projecteuler/challenges/euler005

def Sieve_of_Eratosthenese(n):
    """
    Return list of primes less than n
    """
    res = [2]
    i = 3
    marked = set()
    while i <= n**.5:
        if i not in marked:
            res.append(i)
            j = 0
            while j <= n/i:
                marked.add(i + j*i)
                j += 1
        i += 2
    while i <= n:
        if i not in marked:
            res.append(i)
        i += 2
    return res

def smallest_multiple(n):
    """
    Find all primes less than n
    For each prime, multiply the result by the highest power of the prime less than or equal to n
    """
    if n == 1:
        return 1
    res = 1
    primes = Sieve_of_Eratosthenese(n)
    for p in primes:
        i = 1
        while p**(i+1) <= n:
            i += 1
        res *= p**i
    return res

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(smallest_multiple(n))
