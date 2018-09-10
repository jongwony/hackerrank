def beautifulDays(i, j, k):
    s = 0
    for x in range(i, j+1):
        r = (abs(x - int(str(x)[::-1])) / k)
        if r == int(r):
            s += 1
    return s
