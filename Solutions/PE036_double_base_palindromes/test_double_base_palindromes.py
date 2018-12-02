import unittest
from double_base_palindromes import *


class Test(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome([1, 1]))
        self.assertTrue(is_palindrome([1, 3, 1]))
        self.assertFalse(is_palindrome([1, 3, 1, 3]))

    def test_convert_to_base_k(self):
        self.assertEqual(convert_to_base_k(8, 2), '1000')
        self.assertEqual(convert_to_base_k(1, 2), '1')
        self.assertEqual(convert_to_base_k(3, 2), '11')
        self.assertEqual(convert_to_base_k(11, 2), '1011')

    def test_double_base_palindrome(self):
        self.assertEqual(double_base_palindrome(10**6, 2), 872187)


if __name__ == '__main__':
    unittest.main()
