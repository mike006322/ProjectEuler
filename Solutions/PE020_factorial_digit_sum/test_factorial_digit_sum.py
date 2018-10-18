import unittest
import factorial_digit_sum


class Test(unittest.TestCase):

    def test_factorial_digit_sum(self):
        self.assertEqual(factorial_digit_sum.factorial_digit_sum(3), 6)
        self.assertEqual(factorial_digit_sum.factorial_digit_sum(6), 9)
        self.assertEqual(factorial_digit_sum.factorial_digit_sum(10), 27)


if __name__ == '__main__':
    unittest.main()
