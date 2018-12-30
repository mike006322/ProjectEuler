import unittest
from Solutions.PE041_pandigital_prime.pandigital_prime import *


class Test(unittest.TestCase):

    def test_is_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(31))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(32))

    def test_make_pandigital_primes(self):
        self.assertEqual(make_pandigital_primes(4), {4: [4231, 2341, 2143, 1423]})


if __name__ == '__main__':
    unittest.main()

