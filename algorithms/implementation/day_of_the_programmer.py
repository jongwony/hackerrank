"""
1700 - 1917 julian calendar
1918 1/31 > 2/14 32nd, 256th -> 2/14 + 224
1919 gregorian calendar

both 2/29 leap year
julian: % 4
gregorian: % 400, % 4 and not % 100
format: 'dd.mm.yyyy'

programmers day 256th
9 / 13
9 / 12 leap year
"""

def solve(year):
    months = [31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1700 <= year <= 1917:
        return julian(year, months)
    elif year == 1918:
        return trans(year, months)
    elif year >= 1919:
        return gregorian(year, months)
    else:
        pass


def conv(year, months):
    idx = 0
    days = 0
    while days + months[idx] <= 255:
        days += months[idx]
        idx += 1

    return year, idx + 1, 255 - days


def date_format(year, month, day):
    return '{:02d}.{:02d}.{:04d}'.format(day, month, year)


def julian(year, months):
    if year % 4 == 0:
        months[1] = 28
    return date_format(*conv(year, months))


def gregorian(year, months):
    if year % 400 == 0:
        months[1] = 28
    elif year % 4 == 0 and year % 100 != 0:
        months[1] = 28
    return date_format(*conv(year, months))


def trans(year, months):
    months[1] = 27 - 14 + 1
    return date_format(*conv(year, months))

