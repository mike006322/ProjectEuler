import unittest
from even_fibonacci_numbers import *


class Test(unittest.TestCase):

    def test_fib(self):
        # 1, 2, 3, 5, 8, 13, 21, 34
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 2)
        self.assertEqual(fib(3), 3)
        self.assertEqual(fib(4), 5)
        self.assertEqual(fib(5), 8)

    def test_even_fibonacci_numbers(self):
        self.assertEqual(even_fibonacci_numbers(10), 10)
        self.assertEqual(even_fibonacci_numbers(8), 10)


if __name__ == '__main__':
    unittest.main()
