import unittest
from Solutions.PE015_lattice_paths.python.lattice_paths import *


class Test(unittest.TestCase):

    def test_C(self):
        self.assertEqual(C(2, 0), 1)
        self.assertEqual(C(10, 7), 120)

    def test_lattice_paths(self):
        self.assertEqual(lattice_paths(2, 2), 6)
        self.assertEqual(lattice_paths(2, 3), 10)

    def test_lattice_paths2(self):
        self.assertEqual(lattice_paths2(2, 2), 6)
        self.assertEqual(lattice_paths2(2, 3), 10)


if __name__ == '__main__':
    unittest.main()
