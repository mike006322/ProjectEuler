import unittest
import number_to_words
import sys

class Test(unittest.TestCase):

    def test_break_to_three(self):
        self.assertEqual(number_to_words.break_to_threes(9), ['009'])
        self.assertEqual(number_to_words.break_to_threes(123), ['123'])
        self.assertEqual(number_to_words.break_to_threes(1234), ['001', '234'])
        self.assertEqual(number_to_words.break_to_threes(12345), ['012', '345'])

    def test_spell_last_two(self):
        self.assertEqual(number_to_words.spell_last_two('12'), 'Twelve')
        self.assertEqual(number_to_words.spell_last_two('02'), 'Two')
        self.assertEqual(number_to_words.spell_last_two('23'), 'Twenty Three')

    def test_spell_hundred(self):
        self.assertEqual(number_to_words.spell_hundred('0'), '')
        self.assertEqual(number_to_words.spell_hundred('1'), 'One Hundred ')
        self.assertEqual(number_to_words.spell_hundred('2'), 'Two Hundred ')

    def test_spell_num(self):
        self.assertEqual(number_to_words.spell_num(1010), 'One Thousand Ten ')
        self.assertEqual(number_to_words.spell_num(1010001), 'One Million Ten Thousand One ')

    def test_spell_num2(self):
        self.assertEqual(number_to_words.spell_num2('1010'), 'One Thousand Ten ')
        self.assertEqual(number_to_words.spell_num2('1010001'), 'One Million Ten Thousand One ')

    def test_spell_num3(self):
        number_to_words.spell_num3('12345')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEqual(output,'Twelve Thousand Three Hundred Forty Five')

        print()

        number_to_words.spell_num3('1010001')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEqual(output,'One Million Ten Thousand One')

        print()

        number_to_words.spell_num3('1010')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEqual(output,'One Thousand Ten')

        print()

        number_to_words.spell_num3('200000')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEqual(output,'Two Hundred Thousand')

        print()

        number_to_words.spell_num3('1000000000000')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        self.assertEqual(output,'One Trillion')

if __name__ == '__main__':
    unittest.main()
