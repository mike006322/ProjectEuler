#!/bin/python3

# https://projecteuler.net/problem=17

three_zero_names = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']

tens = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

ones = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ',
        'Twelve ',
        'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']


def spell_num_with_and(num):
    """
    Input is a number as a string type
    Output number spelled out
    """
    res = ''
    if len(num) % 3 == 1:
        num = '00' + num
    elif len(num) % 3 == 2:
        num = '0' + num
    if num == '0':
        return 'Zero'
    else:
        while num:
            a = num[:3]
            num = num[3:]
            if a[0] != '0':
                a = int(a)
                res += ones[a // 100] + 'Hundred '
                a %= 100
                if str(a)[0] != '0':
                    res += 'and '
                    if a < 20:
                        res += ones[a]
                    else:
                        res += tens[a // 10] + ' ' + ones[a % 10]
                    res += three_zero_names[len(num) // 3]
            else:
                a = int(a)
                if a < 20:
                    res += ones[a]
                else:
                    res += tens[a // 10] + ' ' + ones[a % 10]
                if a != 0:
                    res += three_zero_names[len(num) // 3]
    return res


if __name__ == '__main__':
    # print(spell_num3('1000000000000'))
    # print(spell_num3('342'))
    # print(spell_num3('200'))
    # print(spell_num3('242300'))
    s = ''
    for i in range(1, 1001):
        s += spell_num_with_and(str(i)).replace(' ', '')
    print(len(s))
