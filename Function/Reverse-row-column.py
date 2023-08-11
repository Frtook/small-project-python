l = []
U = []
S = []


def forr():
    for i in l:
        for u in i:
            print(u, end=' ')
        print()
    print('After reversing each row:')
    for i in U:
        for u in i:
            print(u, end=' ')
        print()
    print('After reversing each column:')
    for i in S:
        for u in i:
            print(u, end=' ')
        print()
    print()


def s():
    a = len(l[1]) - 1
    for i in range(len(l)):
        S.append(l[-(i + 1)])
        for u in range(len(l[1])):
            U[i][u] = l[i][a]
            a -= 1
        a = len(l) - 1


row = int(input('Enter row:'))
column = int(input('Enter column :'))
for row in range(row):
    P = []
    L = []
    for co in range(column):
        P.append(int(input(f'Enter Nunber {co + 1} : ')))
        L.append(0)
    l.append(P)
    U.append(L)
    print()

s()
forr()
