"""
Given two dates in string format:
    2019-01-01
    2019-01-20

Find the difference between them without using the datetime library
"""


def get_julian_month(month):
    """
    Gets the Julian month; March = 0, April = 1, ... , February = 11

    Args:
        month str: month in 'MM' format

    Returns int: Julian month number

    """

    julian_month = {
        '03': 0,
        '04': 1,
        '05': 2,
        '06': 3,
        '07': 4,
        '08': 5,
        '09': 6,
        '10': 7,
        '11': 8,
        '12': 9,
        '01': 10,
        '02': 11
    }

    return julian_month.get(month)


def get_julian_date(date):
    """
    Gets the Julian date

    Args:
        date str: Date in string format YYYY-MM-DD (2019-01-20)

    Returns int: Julian date

    """

    date_parts = date.split('-')

    month = date_parts[1]

    if month in ['01', '02']:
        year = int(date_parts[0]) - 1
    else:
        year = int(date_parts[0])

    day = int(date_parts[2])

    julian_date = (365*year) + int(year/4) - int(year/100) + int(year/400) + \
                  int(((153 * get_julian_month(month)) + 2)/5) + 1721119 + day

    return julian_date


def date_diff(d1, d2):
    """
    Computes the difference of days between two dates

    Args:
        d1 str: start date in 'YYYY-MM-DD' format
        d2 str: end date in 'YYYY-MM-DD' format

    Returns int: Number of days in between d1 and d2

    """

    return get_julian_date(d2) - get_julian_date(d1)


a = '2019-01-01'
b = '2019-01-20'
print(date_diff(a, b))
# 19

a = '2012-01-01'
b = '2013-01-01'
print(date_diff(a, b))
# 366