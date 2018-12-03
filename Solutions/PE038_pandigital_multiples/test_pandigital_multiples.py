import unittest
from pandigital_multiples import *


class Test(unittest.TestCase):

    def test_pandigital_multiples(self):
        self.assertEqual(pandigital_multiples(100, 8), [18, 78])
        print(pandigital_multiples(1000000, 9))


if __name__ == '__main__':
    unittest.main()
