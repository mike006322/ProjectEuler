import unittest
from digit_Nth_powers import *


class Test(unittest.TestCase):

    def test_find_max_number_of_digits(self):
        self.assertEqual(find_max_number_of_digits(6), 7)

    def test_digit_Nth_powers(self):
        self.assertEqual(digit_Nth_powers(6), 548834)
        print(digit_Nth_powers(5))


if __name__ == '__main__':
    unittest.main()
