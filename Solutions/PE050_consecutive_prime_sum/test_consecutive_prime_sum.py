import unittest
from Solutions.PE050_consecutive_prime_sum.consecutive_prime_sum import *


class Test(unittest.TestCase):

    def test_consecutive_prime_sum(self):
        self.assertEqual(find_max_consecutive_prime_sum_indexed_at_0(1000), (281, 14))
        self.assertEqual(find_max_consecutive_prime_sum_indexed_at_0(1000), (41, 6))


if __name__ == '__main__':
    unittest.main()
