import unittest
from Solutions.PE053_combinatoric_selections.combinatoric_selections import combinatoric_selections


class Test(unittest.TestCase):

    def test_combinatoric_selections(self):
        self.assertEqual(combinatoric_selections(23, 1000000), 4)
        self.assertEqual(combinatoric_selections(100, 1000000), 4075)


if __name__ == '__main__':
    unittest.main()
