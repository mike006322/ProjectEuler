import unittest
import names_scores


class Test(unittest.TestCase):

    def test_divisors(self):
        n = names_scores.Names()
        n.insert('aa')
        n.insert('bb')
        n.sort()
        n.score()
        self.assertEqual(n.namesDict['aa'], 2)
        self.assertEqual(n.namesDict['bb'], 8)

if __name__ == '__main__':
    unittest.main()
