import unittest
from Solutions.PE052_permuted_multiples.permuted_multiples import permuted_multiples


class Test(unittest.TestCase):

    def test_permuted_multiples(self):
        res = "125874 251748 "
        self.assertEqual('\n'.join(permuted_multiples(125875, 2)), res)
        # for item in permuted_multiples(1258750, 6):
        #     print(item)


if __name__ == '__main__':
    unittest.main()
