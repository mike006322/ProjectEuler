import unittest
from Solutions.PE047_distinct_prime_factors.distinct_prime_factors import *
import sys
from io import StringIO


class Test(unittest.TestCase):

    def test_distinct_prime_factors(self):
        sys.stdout = StringIO()
        distinct_prime_factors(20, 2)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertEqual(output, '14\n20')
        sys.stdout = StringIO()
        distinct_prime_factors(644, 3)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertEqual(output, '644')


if __name__ == '__main__':
    unittest.main()
