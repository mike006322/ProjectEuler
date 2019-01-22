import unittest
from Solutions.PE010_summation_of_primes.python.fast_summation import *


class Test(unittest.TestCase):

    def test_prime_sums(self):
        self.assertEqual(prime_sums(11), [0, 0, 2, 5, 5, 10, 10, 17, 17, 17, 17, 28])


if __name__ == '__main__':
    unittest.main()
