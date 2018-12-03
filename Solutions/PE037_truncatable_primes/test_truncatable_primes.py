import unittest
from truncatable_primes import *


class Test(unittest.TestCase):

    def test_remove_digit(self):
        self.assertEqual(remove_digit([2, 0], 'left'), [0])
        self.assertEqual(remove_digit([2, 0], 'right'), [2])
        self.assertEqual(remove_digit([2], 'right'), [])

    def test_truncatable_primes(self):
        self.assertEqual(truncatable_primes(100), 186)
        self.assertEqual(truncatable_primes(10**6), 748317)


if __name__ == '__main__':
    unittest.main()


