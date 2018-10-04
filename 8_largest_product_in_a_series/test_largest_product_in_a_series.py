import unittest
import largest_product_in_a_series

class Test(unittest.TestCase):

    def test_(self):
        self.assertEqual(largest_product_in_a_series.largest_product_in_a_series(1234, 2), 12)
        self.assertEqual(largest_product_in_a_series.largest_product_in_a_series(1234, 4), 24)
        self.assertEqual(largest_product_in_a_series.largest_product_in_a_series(2709360626, 5), 0)

if __name__ == '__main__':
    unittest.main()
