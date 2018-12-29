import unittest
from Solutions.PE040_champerownes_constant.champerownes_constant import *


class Test(unittest.TestCase):

    def test_make_lookup_table(self):
        self.assertEqual(make_lookup_table(4), [(1, 9), (10, 189), (190, 2889), (2890, 38889)])

    def test_find_d_i_n(self):
        lookup_table = make_lookup_table(4)
        self.assertEqual(find_d_i_n(7, lookup_table), 7)
        self.assertEqual(find_d_i_n(12, lookup_table), 1)
        self.assertEqual(find_d_i_n(15, lookup_table), 2)
        self.assertEqual(find_d_i_n(25, lookup_table), 7)
        self.assertEqual(find_d_i_n(2890, lookup_table), 1)


if __name__ == '__main__':
    unittest.main()
