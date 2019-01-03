import unittest
from Solutions.PE043_sub_string_divisibility.sub_string_divisibility import *


class Test(unittest.TestCase):

    def test_pandigital_generator(self):
        self.assertEqual(set(pandigital_generator(2)), {(1, 2, 0), (2, 1, 0), (0, 1, 2), (2, 0, 1), (0, 2, 1), (1, 0, 2)})

    def test_sub_string_divisibility(self):
        print(sub_string_divisibility(3))
        print(sub_string_divisibility(9))


if __name__ == '__main__':
    unittest.main()

