import unittest
from Solutions.PE046_goldbachs_other_conjecture.goldbachs_other_conjecture import *


class Test(unittest.TestCase):

    def test_is_square(self):
        self.assertFalse(is_square(15))
        self.assertTrue(is_square(16))
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(9))

    def test_goldbachs_other_conjecture(self):
        primes = Sieve_of_Eratosthenes(100)
        self.assertEqual(goldbachs_other_conjecture(15, primes), 2)
        self.assertEqual(goldbachs_other_conjecture(9, primes), 1)


if __name__ == '__main__':
    unittest.main()
