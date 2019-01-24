import unittest
from Solutions.PE005_smallest_multiple.python.smallest_multiple import *


class Test(unittest.TestCase):

    def test_multiply_if_not_divide(self):
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_of_eratosthenes(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(10), 2520)
        self.assertEqual(smallest_multiple(1), 1)


if __name__ == '__main__':
    unittest.main()
