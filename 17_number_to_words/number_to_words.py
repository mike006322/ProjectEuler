#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler017

ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
        'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

threes_names = ['Trillion ', 'Billion ', 'Million ', 'Thousand ', '']

def break_to_threes(num):
    """
    input int
    output list of strings representing 3 digits of the number at a time starting with largest values
    if the number of digits is not 0 mod 3 then first str will be less than 3 digits
    """
    num = str(num)
    res = []
    if len(num) % 3 == 0:
        res.append(num[:3])
        num = num[3:]
        while len(num) > 0:
            res.append(num[3:])
            num = num[3:]
    if len(num) % 3 == 1:
        res.append('0' + '0' + num[:1])
        num = num[1:]
        while len(num) > 0:
            res.append(num[:3])
            num = num[3:]
    if len(num) % 3 == 2:
        res.append('0' + num[:2])
        num = num[2:]
        while len(num) > 0:
            res.append(num[:3])
            num = num[3:]
    return res

def spell_last_two(s):
    """
    input is a string of two digits
    output is string of the digits written out
    """
    res = ''
    global ones
    global tens
    if s[0] == '0' or s[0] == '1':
        return ones[int(s)]
    else:
        res += tens[int(s[0])] + ' ' + ones[int(s[1])]
    return res

def spell_hundred(s):
    """
    input is a string of one digit
    output is the number spelled out with "Hundred " appended if not zero
    """
    global ones
    if s == '0':
        return ''
    else:
        return ones[int(s)] + ' ' + 'Hundred '

def spell_num(num):
    """
    input is string
    output is str of number spelled out
    """
    if num == '0':
        return 'Zero'
    res = ''
    threes = break_to_threes(num)
    global threes_names
    for i in range(len(threes)):
        res += spell_hundred(threes[i][0])
        res += spell_last_two(threes[i][1:])
        res += ' ' + threes_names[5 - (len(threes) - i)]
    return res

def spell_num2(num):
    """
    input str representing number
    output str as number spelled out
    """
    if num == '0':
        return 'Zero'
    global ones
    global tens
    global threes_names
    res = ''
    num = (3 - len(num) % 3)*'0' + num
    m = len(num)//3
    i = 0
    while len(num) > 0:
        a = num[:3]
        num = num[3:]
        if len(str(int(a))) == 1:
            res += ones[int(a)]
        elif len(str(int(a))) == 2:
            if int(a) < 20:
                res += ones[int(a)]
            else:
                res += tens[int(a[1])] + ' ' + ones[int(a[2])]
        else:
            res += ones[int(a[0])] + ' Hundred '
            a = a[1:]
            if int(a) < 20:
                res += ones[int(a)]
            else:
                res += tens[int(a[1])] + ' ' + ones[int(a[2])]
        res += ' ' + threes_names[5 - m + i]
        i += 1
    return res

###################################################################################################

tn = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']

tens = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

o = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ',
        'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']

def spell_num3(num):
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
        while num:
            a = num[:3]
            num = num[3:]
            if a[0] != '0':
                a = int(a)
                print(o[a//100] + 'Hundred ', end='')
                a %= 100
                if a < 20:
                    print(o[a], end='')
                else:
                    print(tens[a//10] + ' ' + o[a%10], end ='')
                print(tn[len(num)//3], end ='')
            else:
                a = int(a)
                if a < 20:
                    print(o[a], end='')
                else:
                    print(tens[a//10] + ' ' + o[a%10], end ='')
                if a != 0:
                    print(tn[len(num)//3], end ='')


if __name__ == '__main__':
    # print(spell_num2('45212'))
    spell_num3('1000000000000')
    # t = int(input())
    # for _ in range(t):
    #     num = input()
    #     spell_num3(num)
    #     print()

