import unittest
from Solutions.PE051_prime_digit_replacements.prime_digit_replacements import find_primes_of_n_digits, make_9_number


class Test(unittest.TestCase):

    def test_make_9_number(self):
        self.assertEqual(make_9_number(3), 999)

    def test_find_primes_less_than_n_with_m_digits(self):
        res = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes_of_n_digits(2), res)


if __name__ == '__main__':
    unittest.main()
