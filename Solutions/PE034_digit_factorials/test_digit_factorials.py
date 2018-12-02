import unittest
from digit_factorials import *


class Test(unittest.TestCase):

    def test_digit_factorial(self):
        self.assertEqual(digit_factorial(20), 19)

    def test_digit_factorial_sum(self):
        self.assertEqual(digit_factorial_sum(1000000), 40730)


if __name__ == '__main__':
    unittest.main()
