import unittest
from Solutions.PE008_largest_product_in_a_series.python.largest_product_in_a_series import *


class Test(unittest.TestCase):

    def test_largest_product_in_a_series(self):
        self.assertEqual(largest_product_in_a_series(1234, 2), 12)
        self.assertEqual(largest_product_in_a_series(1234, 4), 24)
        self.assertEqual(largest_product_in_a_series(2709360626, 5), 0)
        self.assertEqual(largest_product_in_a_series(10000023, 2), 6)


    def test_product_of_k_digits(self):
        self.assertEqual(product_of_k_digits(1234, 2, 1), 6)
        self.assertEqual(product_of_k_digits(1023456789, 2, 0), 0)


if __name__ == '__main__':
    unittest.main()
