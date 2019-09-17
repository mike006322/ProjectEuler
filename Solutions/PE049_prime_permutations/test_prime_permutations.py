import unittest
from Solutions.PE049_prime_permutations.prime_permutations import *


class Test(unittest.TestCase):

    def test_prime_permutaitons(self):
        pass

    def test_is_permutation(self):
        self.assertTrue(is_permutation('aba', 'baa'))
        self.assertFalse(is_permutation('aba', 'baaa'))
        self.assertFalse(is_permutation('aba', 'bab'))


if __name__ == '__main__':
    unittest.main()
