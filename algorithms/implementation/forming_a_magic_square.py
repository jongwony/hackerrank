from operator import itemgetter


# Example of magic_squares
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2],
]


def magic_squares():
    """
    Find all cases of magic square
    reflect, transpose, reverse
    """
    reflect = itemgetter(2, 1, 0)
    r = []
    # reflection
    r.append(magic_square)
    r.append(reflect(magic_square))
    r.append(list(map(reflect, magic_square)))
    r.append(list(map(reflect, reflect(magic_square))))
    # transpose(MemoryError if not array copy)
    for mat in r.copy():
        r.append(list(zip(*mat)))
    return r


def formingMagicSquare(s):
    """
    chain array, min distance
    """
    arr = list(chain(*s))
    r = []
    for mat in magic_squares():
        magic_arr = list(chain(*mat))
        r.append(sum(abs(x - y) for x, y in zip(magic_arr, arr)))
    return min(r)

