#https://www.hackerrank.com/contests/projecteuler/challenges/euler008

def product_of_k_digits(n, k, i):
    """
    multiplies k digits of num starting at i
    """
    b = 1
    j = 0
    while j < k:
        b *= int(str(n)[i+j])
        j += 1
    return b


def largest_product_in_a_series(n, k):
    """
    n and k are int
    returns the largest product of k digits from n
    start with the product of the first k digits
    then go through and first divide by the last digit and multiply by the next digit in front
    if the last digit is 0, rebuild the product
    compare the product to the maximum product found so far
    """
    b = product_of_k_digits(n, k, 0)
    i = k
    m = b
    if k < len(str(n)):
        while i < len(str(n)):
            if int(str(n)[i-k]) == 0:
                b = product_of_k_digits(n, k, i - k + 1)
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
