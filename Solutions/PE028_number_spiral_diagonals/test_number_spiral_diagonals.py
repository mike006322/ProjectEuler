import unittest
from number_spiral_diagonals import *


class Test(unittest.TestCase):

    def test_number_spiral_diagonals(self):
        self.assertEqual(number_spiral_diagonals(3), 25)


if __name__ == '__main__':
    unittest.main()
