#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler008


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
    # n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    # print(len(str(n)))
    print(largest_product_in_a_series(n, 13))
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        num = input().strip()
        print(largest_product_in_a_series(num, k))
