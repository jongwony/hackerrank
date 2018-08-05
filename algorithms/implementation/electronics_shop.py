def getMoneySpent(keyboards, drives, b):
    """
    price list `keyboards`, usb `drives`, budget `b`
    print the amount of money
    not enough money print -1
    as much as possible 2 item
    """
    possibles = [k + d for k in keyboards for d in drives if k + d <= b] or [-1]
    return max(possibles)

