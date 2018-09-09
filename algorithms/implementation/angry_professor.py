def angryProfessor(k, a):
    return 'YES' if k > len([x for x in a if x <= 0]) else 'NO'
