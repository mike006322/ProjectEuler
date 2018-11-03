import unittest
from distinct_powers import *


class Test(unittest.TestCase):

    def test_distinct_powers(self):
        self.assertEqual(distinct_powers(8), 44)
        print(distinct_powers(100))

    def test_distinct_powers_naive(self):
        self.assertEqual(distinct_powers_naive(15), 177)

    def test_count_dupes(self):
        self.assertEqual(count_dupes(3, 8), 2)


if __name__ == '__main__':
    unittest.main()
