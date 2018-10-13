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
