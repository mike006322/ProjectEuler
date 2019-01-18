import unittest
from Solutions.PE001_multiples_of_3_and_5.python.multiples_of_3_and_5 import *


class Test(unittest.TestCase):

    def test_multiples_of_3_and_5(self):
        self.assertEqual(multiples_of_3_and_5(15), 45)


if __name__ == '__main__':
    unittest.main()
