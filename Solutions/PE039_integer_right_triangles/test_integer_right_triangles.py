import unittest
from integer_right_triangles import *


def binary_search(alist, item):
    """
    returns the index where the item is in alist. O(logn) time
    # returns the index of element closest to the item that is still <= item in alist
    """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = alist[midpoint]
        elif alist[midpoint-1] <= item < alist[midpoint]:
            found = alist[midpoint-1]
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


class Test(unittest.TestCase):

    def test_integer_right_triangles(self):
        solutions = integer_right_triangles()
        self.assertEqual(solutions[binary_search(list(solutions), 80)], 60)
        self.assertEqual(solutions[binary_search(list(solutions), 12)], 12)
        self.assertEqual(solutions[binary_search(list(solutions), 120)], 120)
        self.assertEqual(solutions[binary_search(list(solutions), 119)], 60)


if __name__ == '__main__':
    unittest.main()
