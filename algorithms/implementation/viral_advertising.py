def viralAdvertising(n):
    i = 1
    a = 5
    r = a // 2
    s = r
    while i < n:
        i += 1
        a = r * 3
        r = a // 2
        s += r
    return s
