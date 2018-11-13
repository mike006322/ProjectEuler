import unittest
from coin_sums import *


class Test(unittest.TestCase):

    def test_coin_sums(self):
        self.assertEqual(coin_sums(10), [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11])


if __name__ == '__main__':
    unittest.main()
