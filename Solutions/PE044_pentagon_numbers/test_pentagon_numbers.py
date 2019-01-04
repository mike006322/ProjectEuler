import unittest
from Solutions.PE044_pentagon_numbers.pentagon_numbers import *


class Test(unittest.TestCase):

    def test_pentagon_number(self):
        self.assertEqual(pentagonal_number(1), 1)
        self.assertEqual(pentagonal_number(2), 5)
        self.assertEqual(pentagonal_number(3), 12)


if __name__ == '__main__':
    unittest.main()
