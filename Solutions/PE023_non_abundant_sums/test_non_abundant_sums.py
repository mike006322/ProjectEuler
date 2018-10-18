import unittest
import non_abundant_sums


class Test(unittest.TestCase):

    def test_non_abundant_sums(self):
        self.assertEqual(len(non_abundant_sums.find_abundant_numbers()), 4994)


if __name__ == '__main__':
    unittest.main()
