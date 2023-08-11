def N(n1, *n2):
    if len(n2) == 0:
        for i in range(2, n1):
            if i % 2 == 0:
                print(i, end=' ')
    else:
        for i in range(n1, n2[0]):
            if i % 2 == 0:
                print(i, end=' ')


N(10, 20)
print()
N(7)
