from counting_sundays import Zeller

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def start_next_month(date):
    """
    input date as (year, month, day)
    output the start of the next month (year, month, day)
    and the number of days until that start
    """
    if date[2] == 1:
        return date, 0
    day = 1
    if date[1] == 12:
        month = 1
        year = date[0] + 1
    else:
        month = date[1] + 1
        year = date[0]
    res = (year, month, day)
    if year % 4 == 0:
        days = leap_year_days[date[1]] - date[2] + 1
    else:
        days = month_days[date[1]] - date[2] + 1
    return res, days

# leap year if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def leap_year(year):
    """
    input in with 4 digits representing year
    output bool whether it is a leap year
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def counting_sundays(start, end):
    """
    input is two days in format (year, month, day)
    output is the number of Sundays that are first days of the month
    """
    # first find out the weekday that start date is
    start_weekday = Zeller(start[0], start[1], start[2])
    # next count by starts of months, keeping track of how many days have elapsed since start
    # if days_elapsed + start_weekday == 6 % 7 then increment res
    first_next_month, days_elapsed = start_next_month(start)
    res = 0
    if end[0] > first_next_month[0] or (end[0] == first_next_month[0] and end[1] > first_next_month[1]):
        y = first_next_month[0]
        m = first_next_month[1]
        while y <= end[0]:
            if y == end[0]:
                while m <= end[1]:
                    if m == end[1]:
                        if (days_elapsed + start_weekday) % 7 == 6:
                            res += 1
                        return res
                    if leap_year(y):
                        if (days_elapsed + start_weekday) % 7 == 6:
                            res += 1
                            m += 1
                            days_elapsed = (days_elapsed + leap_year_days[i]) % 7
                    else:
                        if (days_elapsed + start_weekday) % 7 == 6:
                            res += 1
                            m += 1
                            days_elapsed = (days_elapsed + month_days[i]) % 7
            if leap_year(y):
                for i in range(1, 13):
                    if (days_elapsed + start_weekday) % 7 == 6:
                        res += 1
                    days_elapsed = (days_elapsed + leap_year_days[i]) % 7
            else:
                for i in range(1, 13):
                    if (days_elapsed + start_weekday) % 7 == 6:
                        res += 1
                    days_elapsed = (days_elapsed + month_days[i]) % 7
            y += 1
    else:
        return 0
