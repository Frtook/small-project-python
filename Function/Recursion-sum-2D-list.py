def n(l, x, c):
    while x < len(l):
        if type(l[x]) == type(1):
            c += l[x]
            return n(l, x + 1, c)
        else:
            for i in l[x]:
                c += i
            return n(l, x + 1, c)
    return c


l = [1, 3, [2, 5, 7], [2], 1, 2, 3]
print(n(l, 0, 0))
