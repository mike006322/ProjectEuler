import unittest
import multiples_of_3_and_5

class Test(unittest.TestCase):

    def test_multiples_of_3_and_5(self):
        self.assertEqual(multiples_of_3_and_5.multiples_of_3_and_5(10), 23)

if __name__ == '__main__':
    unittest.main()
