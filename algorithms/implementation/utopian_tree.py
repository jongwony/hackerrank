def utopianTree(n):
    result = [1]
    for i, e in enumerate(range(n)):
        operand = result[-1] + 1 if i % 2 != 0 else result[-1] * 2
        result.append(operand)
    return result[-1]
