import sys


def countingValleys(n, s):
    """
    # https://www.hackerrank.com/challenges/counting-valleys/problem

    uphill, U
    downhill, D
    [DDUUUUDD]
    mountain: above sea level
    valley: below sea level

    :return: number of valleys hike
    """
    step = {'U': 1, 'D': -1}
    valley = 0
    sea_level = 0
    for x in s:
        sea_level += step[x]
        if sea_level == 0 and x == 'U':
            valley += 1

    return valley

