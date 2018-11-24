#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler033

from itertools import combinations_with_replacement as combs
from itertools import combinations
from itertools import permutations
from itertools import product
from math import gcd


def have_i_digits_in_common(n, m, i):
    """
    input two integers and i
    return boolean whether they share i digits in common excluding 0's
    """
    n = list(n)
    m = list(m)
    num_common = 0
    for digit in n:
        if digit in m and digit != '0' and digit != 0:
            m.remove(digit)
            num_common += 1
            if num_common >= i:
                return True
    return False


def find_common_digits(n, m):
    """
    input two integers and i
    returns list common digits as str's excluding 0's
    """
    n = list(n)
    m = list(m)
    res = []
    for digit in n:
        if digit in m:
            m.remove(digit)
            if digit != 0:
                res.append(digit)
    return res


def make_number(digits):
    """
    input tuple of digits
    return int of those digits
    """
    res = 0
    digits = list(digits)
    while digits:
        res *= 10
        res += int(digits.pop(0))
    return res


def find_indicies(number, digit):
    """
    input number as a tuple of strings representing digits and one str digit
    returns all the indicies of the occurances of digit in number
    """
    indicies = []
    for i, n in enumerate(number):
        if n == digit:
            indicies.append(i)
    return indicies


def remove_digits(n, digits):
    """
    input number and digits to be removed
    output set of numbers that are n without the digits
    """
    res = set()
    res.add(n)
    common_digits = list(digits)
    while common_digits:
        d = common_digits.pop()
        new_res = set()
        for number in res:
            occurances = find_indicies(number, d)
            for i in occurances:
                if i == 0:
                    new_res.add(number[1:])
                elif i == len(number)-1:
                    new_res.add(number[:i])
                else:
                    new_res.add(number[:i] + number[i + 1:])
        res = new_res
    n_res = []
    for i in res:
        if make_number(i) != 0:
            n_res.append(make_number(i))
    return n_res


def merge_lists(list1, list2, comb):
    """
    input three lists. Third list represents the spots to put elements of the second list
    merges list2 into list1 based on comb
    """
    comb = list(comb)
    res = []
    list2 = list(list2)
    for i in range(len(list1)):
        while i in comb:
            res.append(list2.pop(0))
            comb.remove(i)
        res.append(list1[i])
    while list2:
        res.append(list2.pop(0))
    return tuple(res)


def permutations_with_order(digits, i):
    """
    input the digits to be included in result and the number of positions to add digits to
    returns digits with i more spots filled with digits 1 to 9 and the extra digits used
    """
    # first find which spots will have digits added to them
    # len(digits) + 1 many places to put i digits
    # comb in combinations(range(len(digits)), i)
    # above will tell you the spots to put extra digits
    # eg, (0,1) means add digits to the front and after the first item
    for comb in combs(range(len(digits) + 1), i):
        for extra_digits in combs((1, 2, 3, 4, 5, 6, 7, 8, 9), i):
            for p_extra_digits in permutations(extra_digits, len(extra_digits)):
                yield merge_lists(digits, p_extra_digits, comb), p_extra_digits


def permutations_with_order_given_extras(digits, extras):
    """
    input the digits to be included in result and the number of positions to add digits to
    returns digits with i more spots filled with digits 1 to 9
    """
    # first find which spots will have digits added to them
    # len(digits) + 1 many places to put i digits
    # comb in combinations(range(len(digits)), i)
    # above will tell you the spots to put extra digits
    # eg, (0,1) means add digits to the front and after the first item
    for comb in combinations(range(len(digits) + 1), len(extras)):
        for extra_digits in combs(extras, len(extras)):
            yield merge_lists(digits, extra_digits, comb)


def digit_canceling_fractions2(N, K):
    """
    passes test cases 0, 1, 2. Times out for 3, 4, 5
    """
    res = []
    fractions = set()
    test_res = []
    tested = set()
    for n in range(10**(N-K-1), 10**(N-K)):
        for m in range(n + 1, 10**(N-K)):
            fractions.add((n, m))
    for fraction in fractions:
        for numerator_digits, extras in permutations_with_order([int(x) for x in str(fraction[0])], K):
            numerator = make_number(numerator_digits)
            for denominator_digits in find_denominator_digits(extras, fraction[1]):
                denominator = make_number(denominator_digits)
                if (numerator, denominator, fraction[0], fraction[1]) in tested:
                    continue
                tested.add((numerator, denominator, fraction[0], fraction[1]))
                if denominator > numerator:
                    if numerator/denominator == fraction[0]/fraction[1]:
                        test_res.append((numerator, denominator, fraction[0], fraction[1]))
                        res.append((numerator, denominator))
    return test_res, sum(x[0] for x in res), sum(x[1] for x in res)


def make_fractions(n):
    """
    returns list of fractions in form [a,b] where b has at most n digits
    """
    res = []
    for b in range(10**(n-1), 10**n):
        for a in range(10**(n-1), b):
            res.append([a, b])
    return res


def digit_canceling_fractions4(N, K):
    """
    works for test cases 0, 1, 2, times out for 3, 4, 5
    """
    res = []
    numerator_sum = 0
    denominator_sum = 0
    all_digits_in_top = list(product(range(10), repeat=N))
    for digits_in_bottom in product(range(10), repeat=N):
        if digits_in_bottom[0] == 0:
            continue
        for digits_in_top in all_digits_in_top:
            if digits_in_top[0] == 0:
                continue
            a = make_number(digits_in_top)
            b = make_number(digits_in_bottom)
            if a >= b:
                break
            shared_digits = find_common_digits(digits_in_top, digits_in_bottom)
            if len(shared_digits) >= K:
                for digits_to_remove in set(combinations(shared_digits, K)):
                    numerators = remove_digits(digits_in_top, digits_to_remove)
                    denominators = remove_digits(digits_in_bottom, digits_to_remove)
                    for numerator in numerators:
                        for denominator in denominators:
                            if a*denominator == numerator*b:
                                numerator_sum += a
                                denominator_sum += b
                                res.append((a, b, numerator, denominator))
    return sum(x[0] for x in res), sum(x[1] for x in res), res
    # return numerator_sum, denominator_sum


def find_digits_to_cancel(numerator_tuple, specific_eq_numerator_tuple):
    res = list(numerator_tuple)
    for x in specific_eq_numerator_tuple:
        res.remove(x)
    return res


def find_denominator_digits(digits_to_cancel, eq_denominator):
    """
    put the digits to cancel among the eq_denominoator digits which must maintain order
    """
    res = set()
    for p_digits_to_cancel in permutations(digits_to_cancel, len(digits_to_cancel)):
        for comb in combs(range(len(p_digits_to_cancel)+1), len(str(eq_denominator))):
            res.add(merge_lists(p_digits_to_cancel, [x for x in str(eq_denominator)], comb))
    return res


def digit_canceling_fractions5(N, K):
    """
    passes test cases 0, 1, and 2. Times out for 3, 4, 5
    """
    res = []
    numerators_seen = set()
    for numerator in range(10**(N-1), 10**N):
        numerator_tuple = tuple(x for x in str(numerator))
        for eq_numerator_tuple in combinations(numerator_tuple, N-K):
            if eq_numerator_tuple == ('0',):
                continue
            # for specific_eq_numerator_tuple in permutations(eq_numerator_tuple, N-K):
            digits_to_cancel = find_digits_to_cancel(numerator_tuple, eq_numerator_tuple)
            if '0' in digits_to_cancel:
                continue
            eq_numerator = make_number(eq_numerator_tuple)
            if (numerator, eq_numerator) in numerators_seen:
                continue
            numerators_seen.add((numerator, eq_numerator))
            for eq_denominator in range(eq_numerator, 10**(N-K)):
                if eq_denominator <= eq_numerator:
                    continue
                # determine denominator digits
                # for each permutation of the denominator
                denominator_tuples = find_denominator_digits(digits_to_cancel, eq_denominator)
                for specific_denominator_tuple in denominator_tuples:
                    denominator = make_number(specific_denominator_tuple)
                    if denominator > numerator:
                        if numerator*eq_denominator == denominator*eq_numerator:
                            res.append((numerator, denominator, eq_numerator, eq_denominator))
    return sum(x[0] for x in res), sum(x[1] for x in res), res


# below are the most time-efficient solutions:

# Explanation: Consider that we want solutions "n/d = n2/d2".
# Iterate through possible values of n which has N digits.
# Then iterate over N-K possible digits from the digits of n (N choose N-K) to make n2.
# Now, consider n/n2. We must have n/n2 = d/d2 and d must have the digit/s of n that n2 doesn't have.
# The clever step is to iterate through fractions that are equal to n/n2;
# this means divide both n and n2 by g = gcd(n, n2)
# and then multiply both n/g and n2 /g by integer i, which you will iterate.
# If we write n/n2 as an ordered pair (n, n2) then the iteration looks like ((n/g)*i, (n2/g)*i), i += 1,
# and for each iteration of i you check if (n/g)*i has the digits of n that n2 doesn't have.


def has_digits(number, digits):
    """
    return boolean whether number has digits in the order that digits is in
    """
    digits = list(digits)
    num = [int(x) for x in str(number)]
    while digits:
        d = digits.pop(0)
        if d in num:
            num.remove(d)
        else:
            return False
    return True


def digit_canceling_fractions_4_3():
    res = set()
    for numerator in range(10**3, 10**4):
        numerator_tuple = tuple(int(x) for x in str(numerator))
        if 0 in numerator_tuple:
            continue
        for digit in set(numerator_tuple):
            if digit == 0:
                continue
            g = gcd(numerator, digit)
            reduced = (numerator // g, digit // g)
            z = 2
            check_digits = list(numerator_tuple)
            check_digits.remove(digit)
            while len(str(reduced[0]*z)) <= 4 and len(str(reduced[1]*z)) <= 1:
                if z == g:
                    z += 1
                    continue
                if len(str(reduced[0]*z)) == 4:
                    if has_digits(reduced[0]*z, check_digits):
                        e = [int(x) for x in str(reduced[0]*z)]
                        for x in check_digits:
                            e.remove(x)
                        e = e.pop()
                        if e in [int(x) for x in str(reduced[1]*z)] and e > digit:
                            res.add((numerator, reduced[0]*z, digit, reduced[1]*z))
                # else:
                #     print(reduced[0]*z)
                z += 1
    return sum(x[0] for x in res), sum(x[1] for x in res), res


def digit_canceling_fractions_4_1():
    res = set()
    for numerator in range(10**3, 10**4):
        numerator_tuple = tuple(int(x) for x in str(numerator))
        for eq_numerator_tuple in set(combinations(numerator_tuple, 3)):
            eq_numerator = make_number(eq_numerator_tuple)
            if eq_numerator == 0:
                continue
            g = gcd(numerator, eq_numerator)
            reduced = (numerator // g, eq_numerator // g)
            z = 1
            check_digits = list(numerator_tuple)
            for digit in eq_numerator_tuple:
                check_digits.remove(digit)
            if check_digits == [0]:
                continue
            while len(str(reduced[0]*z)) <= 4 and len(str(reduced[1]*z)) <= 3:
                if z == g:
                    z += 1
                    continue
                reduced_0_z = reduced[0]*z
                reduced_1_z = reduced[1]*z
                if check_digits[0] in [int(x) for x in str(reduced_0_z)]:
                    eq_denominator_tuple = [int(x) for x in str(reduced_0_z)]
                    for eq_d in remove_digits(tuple(eq_denominator_tuple), check_digits):
                        # eq_denominator_tuple.remove(check_digits[0])
                        # eq_denominator = make_number(eq_d)
                        if reduced_1_z == eq_d and eq_d > eq_numerator:
                            # res.add((numerator, reduced_0_z, eq_numerator, reduced_1_z))
                            res.add((numerator, reduced_0_z))
                z += 1
    return sum(x[0] for x in res), sum(x[1] for x in res), res


def digit_canceling_fractions_4_2():
    res = set()
    for numerator in range(10**3, 10**4):
        numerator_tuple = tuple(int(x) for x in str(numerator))
        for eq_numerator_tuple in set(combinations(numerator_tuple, 2)):
            eq_numerator = make_number(eq_numerator_tuple)
            if eq_numerator == 0:
                continue
            g = gcd(numerator, eq_numerator)
            reduced = (numerator // g, eq_numerator // g)
            z = 1
            check_digits = list(numerator_tuple)
            for digit in eq_numerator_tuple:
                check_digits.remove(digit)
            if 0 in check_digits:
                continue
            while len(str(reduced[0]*z)) <= 4 and len(str(reduced[1]*z)) <= 2:
                if z == g:
                    z += 1
                    continue
                reduced_0_z = reduced[0]*z
                reduced_1_z = reduced[1]*z
                if has_digits(reduced_0_z, check_digits):
                    eq_denominator_tuple = [int(x) for x in str(reduced_0_z)]
                    for eq_d in remove_digits(tuple(eq_denominator_tuple), check_digits):
                        # eq_denominator_tuple.remove(check_digits[0])
                        # eq_denominator = make_number(eq_d)
                        if reduced_1_z == eq_d and eq_d > eq_numerator:
                            # res.add((numerator, reduced_0_z, eq_numerator, reduced_1_z))
                            res.add((numerator, reduced_0_z))
                z += 1
    return sum(x[0] for x in res), sum(x[1] for x in res), res


if __name__ == '__main__':
    N, K = map(int, input().split())
    if N <= 3:
        print(*digit_canceling_fractions5(N, K)[:2])
    elif K == 3:
        print(*digit_canceling_fractions_4_3()[:2])
    elif K == 1:
        print(*digit_canceling_fractions_4_1()[:2])
    elif K == 2:
        print(*digit_canceling_fractions_4_2()[:2])
