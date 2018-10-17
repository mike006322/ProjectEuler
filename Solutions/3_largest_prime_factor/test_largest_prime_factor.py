import unittest
import largest_prime_factor

class Test(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor.largest_prime_factor(14), 7)
        self.assertEqual(largest_prime_factor.largest_prime_factor(100), 5)

if __name__ == '__main__':
    unittest.main()
