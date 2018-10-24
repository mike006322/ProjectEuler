import unittest
import amicable_numbers
import fast_amicable_numbers

class Test(unittest.TestCase):

    def test_divisors(self):
        self.assertEqual(amicable_numbers.divisors(3), [1])
        self.assertEqual(amicable_numbers.divisors(10), [1, 2, 5])
        self.assertEqual(amicable_numbers.divisors(8), [1, 2, 4])
        self.assertEqual(amicable_numbers.divisors(220), [1, 2, 4, 5, 11, 10, 22, 20, 44, 55, 110])

    def test_d(self):
        self.assertEqual(amicable_numbers.d(220), 284)

    def test_amicable_numbers(self):
        self.assertEqual(amicable_numbers.amicable_numbers(300), 504)
        self.assertEqual(amicable_numbers.amicable_numbers(221), 220)

    def test_sum_of_proper_divisors(self):
        primes = fast_amicable_numbers.Sieve_of_Eratosthenes(1000)
        self.assertEqual(fast_amicable_numbers.sum_of_proper_divisors(284, primes), 220)

    def test_fast_sum_of_proper_divisors(self):
        primes = fast_amicable_numbers.Sieve_of_Eratosthenes(1184)
        is_prime = fast_amicable_numbers.Sieve_of_Eratosthenes_TF_List(1184)
        self.assertEqual(fast_amicable_numbers.fast_sum_of_proper_divisors(284, primes, is_prime), 220)
        self.assertEqual(fast_amicable_numbers.fast_sum_of_proper_divisors(220, primes, is_prime), 284)
        self.assertEqual(fast_amicable_numbers.fast_sum_of_proper_divisors(7, primes, is_prime), 1)
        self.assertEqual(fast_amicable_numbers.fast_sum_of_proper_divisors(1184, primes, is_prime), 1210)

    def test_amicable_numbers(self):
        self.assertEqual(fast_amicable_numbers.amicable_numbers(300), {220, 284})
        self.assertEqual(fast_amicable_numbers.amicable_numbers(221), {220})

if __name__ == '__main__':
    unittest.main()
