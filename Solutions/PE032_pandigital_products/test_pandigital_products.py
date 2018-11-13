import unittest
from pandigital_products import *


class Test(unittest.TestCase):

    def test_pandigitial_products(self):
        self.assertEqual(pandigitial_products(4), 12)
        self.assertEqual(pandigitial_products(9), 45228)


if __name__ == '__main__':
    unittest.main()
