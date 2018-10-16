import unittest
import summation_of_primes
class Test(unittest.TestCase):

    def test_summation_of_primes(self):
        self.assertEqual(summation_of_primes.summation_of_primes(10), 17)


if __name__ == '__main__':
    unittest.main()
