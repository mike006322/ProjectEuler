import unittest
from Solutions.PE012_highly_divisible_triangular_number.python.highly_divisible_triangular_number import *


class Test(unittest.TestCase):

    def count_divisors(self):
        primes = sieve_of_eratosthenes(1000000)
        self.assertEqual(count_divisors(11, primes), 2)
        self.assertEqual(count_divisors(6, primes), 4)
        self.assertEqual(count_divisors(28, primes), 6)

    def test_triangle_number_with_more_than_n_divisors(self):
        self.assertEqual(triangle_number_with_more_than_n_divisors(4), {0: 1, 1: 3, 2: 6, 3: 6, 4: 28, 5: 28})


if __name__ == '__main__':
    unittest.main()
