import unittest
import large_sum

class Test(unittest.TestCase):

    def test_large_sum(self):
        nums = [1000000000, 1000000001]
        self.assertEqual(large_sum.large_sum(nums), '2000000001')

if __name__ == '__main__':
    unittest.main()
