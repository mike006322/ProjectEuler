import unittest
import lexicographic_permutations

class Test(unittest.TestCase):

    def test_find_largets_factorial(self):
        self.assertEqual(lexicographic_permutations.find_largest_factorial(120), 5)
        self.assertEqual(lexicographic_permutations.find_largest_factorial(121), 5)
        self.assertEqual(lexicographic_permutations.find_largest_factorial(119), 4)

    def test_convert_to_factorial_base(self):
        self.assertEqual(lexicographic_permutations.convert_to_factorial_base(120), [1, 0, 0, 0, 0, 0])
        self.assertEqual(lexicographic_permutations.convert_to_factorial_base(121), [1, 0, 0, 0, 1, 0])
        self.assertEqual(lexicographic_permutations.convert_to_factorial_base(241), [2, 0, 0, 0, 1, 0])

    def test_permute_by_factorialized_index(self):
        self.assertEqual(lexicographic_permutations.permute_by_factorialized_index('012', [1, 1, 0]), '120')

    def test_convert_to_factorial_base_13(self):
        self.assertEqual(lexicographic_permutations.convert_to_factorial_base_13(120), [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
