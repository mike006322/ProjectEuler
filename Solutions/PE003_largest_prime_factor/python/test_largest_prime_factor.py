import unittest
from Solutions.PE003_largest_prime_factor.python.largest_prime_factor import *


class Test(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(14), 7)
        self.assertEqual(largest_prime_factor(100), 5)


if __name__ == '__main__':
    unittest.main()
