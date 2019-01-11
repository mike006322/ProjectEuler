import unittest
from Solutions.PE044_pentagon_numbers.pentagon_numbers import *


class Test(unittest.TestCase):

    def test_pentagon_number(self):
        self.assertEqual(pentagonal_number(1), 1)
        self.assertEqual(pentagonal_number(2), 5)
        self.assertEqual(pentagonal_number(3), 12)

    def test_is_pentagonal(self):
        p = {1, 5, 12, 22, 35, 51, 70, 92}
        for i in range(1, 100):
            if i in p:
                self.assertTrue(is_pentagonal(i))
            else:
                if is_pentagonal(i):
                    print(i)
                self.assertFalse(is_pentagonal(i))


if __name__ == '__main__':
    unittest.main()
