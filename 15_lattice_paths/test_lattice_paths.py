import unittest
import lattice_paths

class Test(unittest.TestCase):

    def test_C(self):
        self.assertEqual(lattice_paths.C(2,0), 1)
        self.assertEqual(lattice_paths.C(10,7), 120)

    def test_lattice_paths(self):
        self.assertEqual(lattice_paths.lattice_paths(2, 2), 6)
        self.assertEqual(lattice_paths.lattice_paths(2, 3), 10)

    def test_lattice_paths2(self):
        self.assertEqual(lattice_paths.lattice_paths2(2, 2), 6)
        self.assertEqual(lattice_paths.lattice_paths2(2, 3), 10)

if __name__ == '__main__':
    unittest.main()
