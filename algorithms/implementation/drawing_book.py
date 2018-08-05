# https://www.hackerrank.com/challenges/drawing-book/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def pageCount(n, p):
    """
    minimum number turn arrive p
    """
    p1, p2 = map(lambda x: x // 2, [n, p])
    from_n = abs(p1 - p2)
    from_1 = min(p1, p2)
    return min(from_n, from_1)

