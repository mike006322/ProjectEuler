import unittest
from digit_canceling_fractions import *
import time


class Test(unittest.TestCase):

    # def test_have_i_digits_in_common(self):
    #     self.assertEqual(have_i_digits_in_common(2, 2, 1), True)
    #     self.assertEqual(have_i_digits_in_common(22, 22, 2), True)
    #     self.assertEqual(have_i_digits_in_common(22, 23, 2), False)
    #     self.assertEqual(have_i_digits_in_common(23, 23, 2), True)
    #     self.assertEqual(have_i_digits_in_common(220, 220, 3), False)
    #     self.assertEqual(have_i_digits_in_common(20, 12, 1), True)
    #     self.assertEqual(have_i_digits_in_common(203, 102, 2), False)

    # def test_find_common_digits(self):
    #     self.assertEqual(find_common_digits((2, ), (2, )), [2])
    #     self.assertEqual(find_common_digits((2, 0, 1), (2, 1, 0)), [2, 1])
    #     self.assertEqual(find_common_digits((2, 0), (2, 0)), [2])
    #
    # def test_remove_digits(self):
    #     self.assertEqual(remove_digits((2, 2), [2]), [2])
    #     self.assertEqual(remove_digits((1, 2), [1]), [2])
    #     # self.assertEqual(remove_digits(202, ['2']), [20, 2] or [20, 2])
    #     self.assertEqual(remove_digits((1, 8, 7), [1, 8]), [7])
    #     print(remove_digits((3, 3, 2), [3]))
    #     print(remove_digits((6, 6, 4), [6]))
    #
    # def test_find_indicies(self):
    #     self.assertEqual(find_indicies(('2', '2'), '2'), [0, 1])
    #
    # def test_digit_canceling_fractions(self):
    #     # self.assertEqual(digit_canceling_fractions(2, 1), (110, 322))
    #     print(digit_canceling_fractions(2, 1))
    #     print(digit_canceling_fractions(3, 1))

    # def test_merge_lists(self):
    #     self.assertEqual(merge_lists([1, 2, 3], ['a', 'b'], [0, 3]), ('a', 1, 2, 3, 'b'))
    #
    # def test_find_denominator_digits(self):
    #     self.assertEqual(find_denominator_digits(['3', '6'], 2), [('2', '3', '6'), ('3', '2', '6'), ('3', '6', '2'), ('2', '6', '3'), ('6', '2', '3'), ('6', '3', '2')])
    #
    # def test_digit_canceling_fractions2(self):
    #     # print(digit_canceling_fractions2(3, 2))
    #     # print(digit_canceling_fractions5(3, 2))
    #     test_res, n_sum, d_sum = digit_canceling_fractions2(3, 2)
    #     # print(n_sum, d_sum)
    #     # # n_sum, d_sum, test_res = digit_canceling_fractions4(3, 2)
    #     tr = set(test_res)
    #     # # print(digit_canceling_fractions4(3, 1))
    #     # # print(digit_canceling_fractions5(3, 1))
    #     #
    #     print(set(digit_canceling_fractions5(3, 2)[2]).difference(tr))
    #     print(tr.difference(set(digit_canceling_fractions5(3, 2)[2])))
    #
        # for i in test_res:
        #     print(i)

    # def test_permutations_with_order(self):
    #     self.assertEqual(list(permutations_with_order((1,), 1)), [((1, 1), (1,)), ((2, 1), (2,)), ((3, 1), (3,)), ((4, 1), (4,)), ((5, 1), (5,)), ((6, 1), (6,)), ((7, 1), (7,)), ((8, 1), (8,)), ((9, 1), (9,)), ((1, 1), (1,)), ((1, 2), (2,)), ((1, 3), (3,)), ((1, 4), (4,)), ((1, 5), (5,)), ((1, 6), (6,)), ((1, 7), (7,)), ((1, 8), (8,)), ((1, 9), (9,))])

    # def test_make_fractions(self):
    #     self.assertEqual(len(make_fractions(2)), 4005)
    #     self.assertEqual(type(make_fractions(2)[0]), list)
    #     print(make_fractions(1))
    #

    # def test_digit_canceling_fractions4(self):
    #     print(digit_canceling_fractions4(2, 1))
    #     # start = time.time()
    #     # print(digit_canceling_fractions4(3, 1))
    #     # end = time.time()
    #     # elapsed = end - start
    #     # print('time elapsed: ', elapsed)

    # def test_digit_canceling_fractions5(self):
    #     # print(digit_canceling_fractions5(2, 1))
    #     start = time.time()
    #     print(digit_canceling_fractions5(4, 3))
    #     end = time.time()
    #     elapsed = end - start
    #     print('time elapsed: ', elapsed)

    # def test_has_digits(self):
    #     self.assertTrue(has_digits(132, (1, 3)))
    #     self.assertTrue(has_digits(7231, (1, 3, 2)))
    #     self.assertTrue(has_digits(6937, (3, 9, 6)))
    #     self.assertTrue(has_digits(693, (3, 9, 6)))
    #     self.assertTrue(has_digits(8693, (3, 9, 6)))

    # def test_digit_canceling_fractions_4_3(self):
    #     # tr = set(digit_canceling_fractions5(4, 3)[2])
    #     # print(tr.difference(digit_canceling_fractions_4_3()[2]))
    # #     print((3964, 6937, 4, 7) in digit_canceling_fractions_4_3()[2])
    # #     print((4132, 7231, 4, 7) in digit_canceling_fractions_4_3()[2])
    # #     print(digit_canceling_fractions_4_3())
    #     print(*digit_canceling_fractions_4_3()[:2])

    def test_digit_canceling_fractions_4_1(self):
        # start = time.time()
        # print(digit_canceling_fractions_4_1())
        # end = time.time()
        # elapsed = end - start
        # print('time elapsed: ', elapsed)
        self.assertEqual(digit_canceling_fractions_4_1()[:2], (12999936, 28131911))

    def test_digit_canceling_fractions_4_2(self):
        # start = time.time()
        # print(digit_canceling_fractions_4_2())
        # end = time.time()
        # elapsed = end - start
        # print('time elapsed: ', elapsed)
        self.assertEqual(digit_canceling_fractions_4_2()[:2], (3571225, 7153900))


if __name__ == '__main__':
    unittest.main()
