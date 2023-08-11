def count_even(*a):
    a = list(*a)
    e = 0
    for i in a:
        if i % 2 == 0:
            e += 1
    return e


print(count_even([1, 5, 3, 7]))
