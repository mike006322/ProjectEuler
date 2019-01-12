import unittest
from Solutions.PE017_number_to_words.number_to_words import *
import sys
from io import StringIO


class Test(unittest.TestCase):

    def test_break_to_three(self):
        self.assertEqual(break_to_threes(9), ['009'])
        self.assertEqual(break_to_threes(123), ['123'])
        self.assertEqual(break_to_threes(1234), ['001', '234'])
        self.assertEqual(break_to_threes(12345), ['012', '345'])

    def test_spell_last_two(self):
        self.assertEqual(spell_last_two('12'), 'Twelve')
        self.assertEqual(spell_last_two('02'), 'Two')
        self.assertEqual(spell_last_two('23'), 'Twenty Three')

    def test_spell_hundred(self):
        self.assertEqual(spell_hundred('0'), '')
        self.assertEqual(spell_hundred('1'), 'One Hundred ')
        self.assertEqual(spell_hundred('2'), 'Two Hundred ')

    def test_spell_num(self):
        self.assertEqual(spell_num(1010), 'One Thousand Ten ')
        self.assertEqual(spell_num(1010001), 'One Million Ten Thousand One ')

    def test_spell_num2(self):
        self.assertEqual(spell_num2('1010'), 'One Thousand Ten ')
        self.assertEqual(spell_num2('1010001'), 'One Million Ten Thousand One ')

    def test_spell_num3(self):
        # sys.stdout = StringIO()
        # print(spell_num3('12345'))
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        # self.assertEqual(output, 'Twelve Thousand Three Hundred and Forty Five')
        self.assertEqual(spell_num3('12345').strip(), 'Twelve Thousand Three Hundred and Forty Five')
        #
        # print()
        #
        # spell_num3('1010001')
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()
        # self.assertEqual(output, 'One Million Ten Thousand One')
        #
        # print()
        #
        # spell_num3('1010')
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()
        # self.assertEqual(output, 'One Thousand Ten')
        #
        # print()
        #
        # spell_num3('200000')
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()
        # self.assertEqual(output, 'Two Hundred Thousand')
        #
        # print()
        #
        # spell_num3('1000000000000')
        # if not hasattr(sys.stdout, "getvalue"):
        #     self.fail("need to run in buffered mode")
        # output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        # self.assertEqual(output, 'One Trillion')


if __name__ == '__main__':
    unittest.main()
