import unittest
import fast_summation

class Test(unittest.TestCase):

    def test_prime_sums(self):
        self.assertEqual(fast_summation.prime_sums(11), [0, 0, 2, 5, 5, 10, 10, 17, 17, 17, 17, 28])


if __name__ == '__main__':
    unittest.main()
