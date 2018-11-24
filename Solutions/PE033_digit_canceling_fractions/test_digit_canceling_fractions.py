import unittest
from digit_canceling_fractions import *


class Test(unittest.TestCase):

    def test_remove_digits(self):
        self.assertEqual(remove_digits((2, 2), [2]), [2])
        self.assertEqual(remove_digits((1, 2), [1]), [2])
        # self.assertEqual(remove_digits(202, ['2']), [20, 2] or [20, 2])
        self.assertEqual(remove_digits((1, 8, 7), [1, 8]), [7])
        self.assertEqual(remove_digits((3, 3, 2), [3]), [32])
        self.assertEqual(remove_digits((6, 6, 4), [6]), [64])

    def test_find_indicies(self):
        self.assertEqual(find_indices(('2', '2'), '2'), [0, 1])

    def test_has_digits(self):
        self.assertTrue(has_digits(132, (1, 3)))
        self.assertTrue(has_digits(7231, (1, 3, 2)))
        self.assertTrue(has_digits(6937, (3, 9, 6)))
        self.assertTrue(has_digits(693, (3, 9, 6)))
        self.assertTrue(has_digits(8693, (3, 9, 6)))

    def test_digit_canceling_fractions(self):
        self.assertEqual(digit_canceling_fractions(4, 2), (3571225, 7153900))
        self.assertEqual(digit_canceling_fractions(4, 1), (12999936, 28131911))
        self.assertEqual(digit_canceling_fractions(4, 3), (255983, 467405))
        self.assertEqual(digit_canceling_fractions(3, 1), (77262, 163829))
        self.assertEqual(digit_canceling_fractions(2, 1), (110, 322))


if __name__ == '__main__':
    unittest.main()
