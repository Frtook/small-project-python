a = int(input('Enter Number of List :'))
l = []
for i in range(0, a):
    l.append(int(input(f'Enter Number {i + 1} : ')))
n = int(input('\nfund Number in List Enter Number :'))


def N(e):
    if e in l:
        return True
    else:
        return False


print(N(n))
