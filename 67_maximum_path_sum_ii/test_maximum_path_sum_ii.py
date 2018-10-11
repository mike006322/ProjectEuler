import unittest
import maximum_path_sum_ii

class Test(unittest.TestCase):

    def test_max_path_sum(self):
        self.assertEqual(maximum_path_sum_ii.max_path_sum([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23)

if __name__ == '__main__':
    unittest.main()
