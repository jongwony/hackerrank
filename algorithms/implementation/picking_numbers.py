from functools import reduce
from collections import Counter
from itertools import combinations

def pickingNumbers(a):
    c = Counter(a)
    pick_lists = [c[k] for k in c]
    pick_lists += [c[x] + c[y] for x, y in combinations(c, 2) if abs(x - y) <= 1]
    return max(pick_lists)

def PickingNumbersSolution(a):
    c = Counter(a)
    return reduce(lambda x, y: max(x, c[y] + c[y+1]), c, -1)

