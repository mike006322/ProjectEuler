import unittest
from Solutions.PE048_self_powers.self_powers import *


class Test(unittest.TestCase):

    def test_self_powers(self):
        self.assertEqual(self_powers(10), 405071317)
        # print(time_function(self_powers, [10**5+100]))
        # print(self_powers(1000))


if __name__ == '__main__':
    unittest.main()
