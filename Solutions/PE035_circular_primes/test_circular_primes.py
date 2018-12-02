import unittest
from circular_primes import *

class Test(unittest.TestCase):

    def test_rotations(self):
        self.assertEqual(rotations([1, 7, 9]), {(7, 9, 1), (1, 7, 9), (9, 1, 7)})

    def test_circular_primes(self):
        self.assertEqual(circular_primes(80), 349)
        self.assertEqual(circular_primes(100), 446)
        self.assertEqual(circular_primes(10**6), 8184200)


if __name__ == '__main__':
    unittest.main()
