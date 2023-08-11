def N():
    a = int(input('Enter Number if prime or No : '))
    for i in range(2, a):
        if a % i == 0:
            return True
    else:
        return False


print(N())
