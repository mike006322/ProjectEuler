import unittest
import power_digit_sum

class Test(unittest.TestCase):

    def test_power_digit_sum(self):
        self.assertEqual(power_digit_sum.power_digit_sum(9), 8)

    def test_power_digit_sum_small(self):
        self.assertEqual(power_digit_sum.power_digit_sum_small(9), 8)

if __name__ == '__main__':
    unittest.main()
