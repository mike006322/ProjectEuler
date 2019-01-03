import unittest
from Solutions.PE042_coded_triangle_numbers.coded_triangle_numbers import *


class Test(unittest.TestCase):

    def test_coded_triangle_numbers(self):
        self.assertEqual(coded_triangle_numbers(3), 2)
        self.assertEqual(coded_triangle_numbers(6), 3)
        self.assertEqual(coded_triangle_numbers(4), -1)


if __name__ == '__main__':
    unittest.main()

