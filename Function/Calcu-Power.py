def power(x, n):
    r = 1
    if type(n) or type(x) == float:
        print(x ** n)

    else:
        while n:
            r *= x
            n -= 1
        print(r)


power(2, 3)
power(2, 0.6)
