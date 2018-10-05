import unittest
import longest_collatz_sequence
from functools import lru_cache

class Test(unittest.TestCase):

    def test_next_collatz(self):
        n = 20
        self.assertEqual(longest_collatz_sequence.next_collatz(n), 10)
        self.assertEqual(n, 20)

    def test_longest_collatz_sequence(self):
        self.assertEqual(longest_collatz_sequence.longest_collatz_sequence(10), 9)

    def test_longest_collatz_sequence_so_far(self):
        self.assertEqual(longest_collatz_sequence.longest_collatz_sequence_so_far(10), [1, 1, 2, 3, 3, 3, 6, 7, 7, 9, 9])

    def test_collatz_sequence_length(self):
        self.assertEqual(longest_collatz_sequence.collatz_sequence_length(9), 20)

if __name__ == '__main__':
    unittest.main()
