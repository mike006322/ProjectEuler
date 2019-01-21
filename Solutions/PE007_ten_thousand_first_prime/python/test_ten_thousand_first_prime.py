import unittest
from Solutions.PE007_ten_thousand_first_prime.python.ten_thousand_first_prime import *


class Test(unittest.TestCase):

    def test_(self):
        first_10000_primes = sieve_of_eratosthenes(104729)
        self.assertEqual(len(first_10000_primes), 10000)


if __name__ == '__main__':
    unittest.main()
