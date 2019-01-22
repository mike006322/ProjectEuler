import unittest
from Solutions.PE009_special_pythagorean.python.special_pythagorean import *


class Test(unittest.TestCase):

    def test_generate_primitive_pythagorean_triples(self):
        self.assertEqual(generate_primitive_pythagorean_triples(30), [{3, 4, 5}, {6, 8, 10}, {5, 12, 13}])
        # all 16 primitive triples with hypotenuse less than 100:
        # {3, 4,5}, {5, 12, 13}, {8, 15, 17}, {7, 24, 25}, {20, 21, 29}, {12, 35, 37}, {9, 40, 41}, {28, 45, 53}, {11, 60, 61}, {33, 56, 65}, {16, 63, 65}, {48, 55, 73}, {36, 77, 85}, {13, 84, 85}, {39, 80, 89}, {65, 72, 97}
        self.assertIn({3, 4, 5}, generate_primitive_pythagorean_triples(100))
        self.assertIn({12, 35, 37}, generate_primitive_pythagorean_triples(100))
        self.assertIn({8, 15, 17}, generate_primitive_pythagorean_triples(100))
        self.assertIn({9, 40, 41}, generate_primitive_pythagorean_triples(100))
        self.assertIn({12, 35, 37}, generate_primitive_pythagorean_triples(100))

    def test_check_multiples_of_primitives(self):
        self.assertEqual(check_multiples_of_primitives([{3, 4, 5}, {6, 8, 10}, {5, 12, 13}], 12), {(3, 4, 5)})

    def test_choose_largest(self):
        self.assertEqual(choose_largest({(3, 4, 5), (5, 12, 13)}), 5*12*13)

    def test_special_pythagorean(self):
        self.assertEqual(special_pythagorean(12), 60)
        self.assertEqual(special_pythagorean(4), -1)
        self.assertEqual(special_pythagorean(65 + 72 + 97), 65*72*97)
        self.assertEqual(special_pythagorean(36 + 77 + 85), 36*77*85)
        self.assertEqual(special_pythagorean(33 + 56 + 65), 33*56*65)
        self.assertEqual(special_pythagorean(2*(33 + 56 + 65)), 2**3*33*56*65)


if __name__ == '__main__':
    unittest.main()
