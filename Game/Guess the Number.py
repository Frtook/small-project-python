from random import randint

print('Enter Number "The Number berween 0 to 1000 ": ')
r = randint(0, 100)
c = 1
while True:
    n = int(input(f'Enter Number {c} : '))
    if r > n:
        print('low')
        c += 1
    elif r < n:
        print('high')
        c += 1
    else:
        print('Right')
        print(f'Your tries is {c}')
        break
