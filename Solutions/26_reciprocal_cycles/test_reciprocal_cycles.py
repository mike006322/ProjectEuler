import unittest
import reciprocal_cycles

class Test(unittest.TestCase):

    def test_division_algorithm(self):
        self.assertEqual(reciprocal_cycles.division_algorithm(3, 2), (1, 1))
        self.assertEqual(reciprocal_cycles.division_algorithm(10, 8), (1, 2))
        self.assertEqual(reciprocal_cycles.division_algorithm(15, 7), (2, 1))
        self.assertEqual(reciprocal_cycles.division_algorithm(1, 7), (0, 1))

    def test_find_cycle_length(self):
        self.assertEqual(reciprocal_cycles.find_cycle_length(3), 1)
        self.assertEqual(reciprocal_cycles.find_cycle_length(6), 1)
        self.assertEqual(reciprocal_cycles.find_cycle_length(7), 6)
        self.assertEqual(reciprocal_cycles.find_cycle_length(17), 16)

    def test_reciprocal_cycles(self):
        self.assertEqual(reciprocal_cycles.reciprocal_cycles(5), [0, 0, 0, 3, 3, 3])
        ten = [0, 0, 0, 3, 3, 3, 3, 7, 7, 7, 7]
        self.assertEqual(reciprocal_cycles.reciprocal_cycles(10), ten)
        seventeen = [0, 0, 0, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 17]
        self.assertEqual(reciprocal_cycles.reciprocal_cycles(17), seventeen)

if __name__ == '__main__':
    unittest.main()
