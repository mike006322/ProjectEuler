#https://www.hackerrank.com/contests/projecteuler/challenges/euler008

def largest_product_in_a_series(n, k):
    """
    n and k are int
    returns the largest product of k digits from n
    start with the product of the first k digits
    then go through and first divide by the last digit and multiply by the next digit in front
    if the last digit is 0, rebuild the product
    compare the product to the maximum product found so far
    """
    i = 0
    b = 1
    while i < k:
        b *= int(str(n)[i])
        i += 1
    i = k
    m = b
    if k < len(str(n)):
        while i < len(str(n)):
            if int(str(n)[i-k]) == 0:
                j = 1
                b = 1
                while j < k:
                    b *= int(str(n)[i-k+j])
                    j += 1
            else:
                b //= int(str(n)[i-k])
            b *= int(str(n)[i])
            if b > m:
                m = b
            i += 1
    return m

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        num = input().strip()
        print(largest_product_in_a_series(num, k))
