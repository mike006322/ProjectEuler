import unittest
import highly_divisible_triangular_number

class Test(unittest.TestCase):

    def test_count_divisors(self):
        self.assertEqual(highly_divisible_triangular_number.count_divisors(11), 2)
        self.assertEqual(highly_divisible_triangular_number.count_divisors(6), 4)

    def test_triangle_number_with_n_divisors(self):
        self.assertEqual(highly_divisible_triangular_number.triangle_number_with_n_divisors(4), 28)

    def test_triangle_number_with_more_than_n_divisors(self):
        self.assertEqual(highly_divisible_triangular_number.triangle_number_with_more_than_n_divisors(4), {0: 1, 1: 3, 2: 6, 3: 6, 4: 28, 5: 28})

    def test_fast_count_divisors(self):
        primes = highly_divisible_triangular_number.Sieve_of_Eratostheneses(1000000)
        self.assertEqual(highly_divisible_triangular_number.fast_count_divisors(11, primes), 2)
        self.assertEqual(highly_divisible_triangular_number.fast_count_divisors(6, primes), 4)
        self.assertEqual(highly_divisible_triangular_number.fast_count_divisors(28, primes), 6)


if __name__ == '__main__':
    unittest.main()
