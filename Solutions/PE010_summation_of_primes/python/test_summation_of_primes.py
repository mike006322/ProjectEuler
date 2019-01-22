import unittest
from Solutions.PE010_summation_of_primes.python.summation_of_primes import *


class Test(unittest.TestCase):

    def test_summation_of_primes(self):
        self.assertEqual(summation_of_primes(10), 17)


if __name__ == '__main__':
    unittest.main()
