import unittest
from Solutions.PE006_sum_square_difference.python.sum_square_difference import *


class Test(unittest.TestCase):

    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference(10), 2640)


if __name__ == '__main__':
    unittest.main()
