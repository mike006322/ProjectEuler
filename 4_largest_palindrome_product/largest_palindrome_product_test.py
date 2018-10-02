import unittest
import largest_palindrome_product

class Test(unittest.TestCase):

    def test_next_palindrome(self):
        self.assertEqual(largest_palindrome_product.next_palindrome(799997), 798897)
