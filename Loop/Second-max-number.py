L = []
i = int(input('Enter any number or -1 to exit : '))
while i != -1:
    if i not in L:
        L.append(i)
    i = int(input('Enter any number or -1 to exit : '))
L.remove(max(L))
print(max(L))
