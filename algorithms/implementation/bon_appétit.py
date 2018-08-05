"""
https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen

Anna Brian sharing meal, split the bill equally
Anna allergic -> won't pay
:return: refund pay
"""


def bonAppetit(bill, k, b):
    bill.pop(k)
    if sum(bill) / 2 == b:
        print('Bon Appetit')
    else:
        print(b - sum(bill) // 2)
