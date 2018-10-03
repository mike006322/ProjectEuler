import unittest
import largest_palindrome_product

class Test(unittest.TestCase):

    def test_next_palindrome(self):
        self.assertEqual(largest_palindrome_product.next_palindrome(799997), 798897)

    def test_has_three_digit_factors(self):
        self.assertEqual(largest_palindrome_product.has_three_digit_factors(250000), True)

    def test_has_three_digit_factors(self):
        self.assertEqual(largest_palindrome_product.has_three_digit_factors(800000), False)

    def test_largest_palindrome_product(self):
        self.assertEqual(largest_palindrome_product.largest_palindrome_product(800000), 793397)

if __name__ == '__main__':
    unittest.main()
