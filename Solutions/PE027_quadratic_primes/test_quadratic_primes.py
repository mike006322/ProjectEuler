import unittest
import quadratic_primes

def fast_Sieve_of_Eratosthenes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]

primes = fast_Sieve_of_Eratosthenes(2000)

class Test(unittest.TestCase):

    def test_how_many_primes(self):
        global primes
        self.assertEqual(quadratic_primes.how_many_primes(-1, 41, primes), 42)

    def test_quadratic_primes(self):
        res_42 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (-1, 41)]
        self.assertEqual(quadratic_primes.quadratic_primes(42), res_42)
        print(quadratic_primes.quadratic_primes(50))


if __name__ == '__main__':
    unittest.main()
