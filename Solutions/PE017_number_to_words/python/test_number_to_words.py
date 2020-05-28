import unittest
from Solutions.PE017_number_to_words.python.number_to_words import *
import sys
from io import StringIO


class Test(unittest.TestCase):

    def test_spell_num(self):
        sys.stdout = StringIO()
        # print(spell_num('12345'))
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        # self.assertEqual(output, 'Twelve Thousand Three Hundred Forty Five')
        # # self.assertEqual(spell_num('12345').strip(), 'Twelve Thousand Three Hundred Forty Five')

        spell_num('1010001')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertEqual(output, 'One Million Ten Thousand One')

        # spell_num('1000000000000')
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        # self.assertEqual(output, 'One Trillion')


if __name__ == '__main__':
    unittest.main()
