import unittest
import ten_thousand_first_prime

class Test(unittest.TestCase):

    def test_(self):
        first_10000_primes = ten_thousand_first_prime.Sieve_of_Eratostheneses(104729)
        self.assertEqual(len(first_10000_primes), 10000)

if __name__ == '__main__':
    unittest.main()
