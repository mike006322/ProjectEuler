#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler019

# Python datetime throws error for dates way into the future
# Georgian calendar repeats itself every 400 years
# Georgian calendar + days of week repeat every 2800 years

def next_month(date):
    """
    input date as (year, month, day)
    output (year, month) of next 1st
    """
    if date[2] == 1:
        return date[0], date[1]
    if date[1] == 12:
        month = 1
        year = date[0] + 1
    else:
        month = date[1] + 1
        year = date[0]
    return year, month

def Zeller(y, m, d):
    """
    input three integers representing date as year, month, day
    output is integer representing day of week, Sunday = 6
    """
    # If January or February is entered you must add
    # 12 to the month and subtract 1 from the year.
    # This puts you in month 13 or 14 of previous year.
    if m == 1 or m == 2:
        m += 12
        y -= 1
    century = (y//100)
    century_year = (y % 100)
    return (d + ((26 * (m + 1)) //10) + century_year + (century_year//4) + (century//4) + 5*century - 2) % 7

def counting_sundays(start, end):
    """
    input is two days in format (year, month, day)
    output is the number of Sundays that are first days of the month
    """
    y, m = next_month(start)
    res = 0
    while y < end[0]:
        if y == next_month(start)[0]:
            while m <= 12:
                if Zeller(y, m, 1) == 6:
                    res += 1
                m += 1
            y += 1
        else:
            for i in range(1, 13):
                if Zeller(y, i, 1) == 6:
                    res += 1
            y += 1
    if next_month(start)[0] < end[0]:
        m = 1
    while m <= end[1]:
        if Zeller(y, m, 1) == 6:
                res += 1
        m += 1
    return res

if __name__ == '__main__':
    print(counting_sundays((1901, 1, 1), (2000, 12, 31)))
    # t = int(input())
    # for _ in range(t):
    #     start = tuple(map(int, input().split()))
    #     end = tuple(map(int, input().split()))
    #     print(counting_sundays(start, end))
