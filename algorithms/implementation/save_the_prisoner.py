def saveThePrisoner(n, m, s):
    return (s - 1 + m % n) % n or n
