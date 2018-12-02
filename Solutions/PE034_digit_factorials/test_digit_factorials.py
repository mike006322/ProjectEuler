import unittest
from digit_factorials import *


class Test(unittest.TestCase):

    def test_digit_factorial(self):
        self.assertEqual(digit_factorial(20), 19)

if __name__ == '__main__':
    unittest.main()
