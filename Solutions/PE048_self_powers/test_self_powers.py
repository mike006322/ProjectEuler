import unittest
from Algorithms.python.running_time import *
from Solutions.PE048_self_powers.self_powers import *

self_powers = running_time(self_powers)


class Test(unittest.TestCase):

    def test_self_powers(self):

        print(self_powers(10))
        self.assertEqual(self_powers(10), 405071317)
        self_powers(10**5+100)
        print(self_powers.running_time)


if __name__ == '__main__':
    unittest.main()
