# https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def sockMerchant(n, ar):
    """
    print the total number of matching pairs :ar:
    """
    c = Counter(ar)
    return sum(v // 2 for _, v in c.items())
