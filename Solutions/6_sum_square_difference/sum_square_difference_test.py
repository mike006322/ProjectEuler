import unittest
import sum_square_difference

class Test(unittest.TestCase):

    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference.sum_square_difference(10), 2640)

if __name__ == '__main__':
    unittest.main()
