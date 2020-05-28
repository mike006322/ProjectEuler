#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler017

tens = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

tn = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']

ones = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ',
        'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']


def spell_num(num):
    """
    input string
    output spelled out
    """
    if len(num) % 3 == 1:
        num = '00' + num
    elif len(num) % 3 == 2:
        num = '0' + num
    if num == '0':
        return 'Zero'
    else:
        already_said = False
        while num:
            a = num[:3]
            num = num[3:]
            if a[0] != '0':
                a = int(a)
                print(ones[a // 100] + 'Hundred ', end='')
                a %= 100
                if a < 20:
                    print(ones[a], end='')
                else:
                    print(tens[a // 10] + ' ' + ones[a % 10], end='')
                print(tn[len(num) // 3], end='')
            else:
                a = int(a)
                if a < 20:
                    print(ones[a], end='')
                else:
                    print(tens[a // 10] + ' ' + ones[a % 10], end='')
                if a != 0:
                    print(tn[len(num) // 3], end='')


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        spell_num(input())
        print()
