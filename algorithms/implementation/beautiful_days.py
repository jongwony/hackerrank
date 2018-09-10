def beautifulDays(i, j, k):
    r = 0
    for x in range(i, j+1):
        r += not abs(x - int(str(x)[::-1])) % k
    return r
