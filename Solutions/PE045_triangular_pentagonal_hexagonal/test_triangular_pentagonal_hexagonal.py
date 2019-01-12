import unittest
import sys
from io import StringIO
from Solutions.PE045_triangular_pentagonal_hexagonal.triangular_pentagonal_hexagonal import *


class Test(unittest.TestCase):

    def test_triangular_pentagonal_hexagonal(self):
        sys.stdout = StringIO()
        triangular_pentagonal_hexagonal(10000, 3, 5)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertEqual(output, '1\n210')
        sys.stdout = StringIO()
        triangular_pentagonal_hexagonal(100000, 5, 6)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertEqual(output, '1\n40755')

    def test_is_triangular(self):
        t = {1, 3, 6, 10, 15}
        for i in range(1, 16):
            if i in t:
                self.assertTrue(is_triangular(i))
            else:
                self.assertFalse(is_triangular(i))


if __name__ == '__main__':
    unittest.main()

