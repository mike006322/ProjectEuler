import unittest
from Solutions.PE011_largest_product_in_a_grid.python.largest_product_in_a_grid import *


class Test(unittest.TestCase):

    def test_make_matrix(self):
        self.assertEqual(make_matrix((0, 1, 2, 3)), [[True, True, True, True], [False, False, False, False], [False, False, False, False], [False, False, False, False]])

    def test_matrix_embed(self):
        M = [[True, False, False, True], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
        embedded = [[False, False, False, False, False, False], [False, True, False, False, True, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False]]
        self.assertEqual(matrix_embed(M), embedded)

    def test_check_adjacency(self):
        M = [[True, True, True, True], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
        M2 = [[True, False, False, True], [False, False, False, False], [False, False, False, False], [True, False, False, True]]
        self.assertEqual(check_adjacency(M), True)
        self.assertEqual(check_adjacency(M2), False)

    def test_trim_shape(self):
        M = [[True, True, True, True], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
        M2 = [[True, True, True, True]]
        M3 = [[True, True, True, False], [True, False, False, False], [False, False, False, False], [False, False, False, False]]
        M4 = [[True, True, True], [True, False, False]]
        self.assertEqual(trim_shape(M), M2)
        self.assertEqual(trim_shape(M3), M4)

    def test_look_for_shape(self):
        grid = list()
        grid.append([1]*20)
        for i in range(19):
            grid.append([0]*20)
        # print(grid)
        # print(look_for_shape([[True]*4], grid))
        self.assertEqual(look_for_shape([[True]*4], grid), 1)


if __name__ == '__main__':
    unittest.main()
