def c(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return 'Error'
        return n1 / n2
    elif op == '%':
        if n2 == 0:
            return 'Error'
        return n1 + n2
    else:
        return "ERROR: Invalid Operation"


print(c(3, 2, '+'))
print(c(3, 2, '-'))
print(c(3, 2, '*'))
print(c(3, 2, '/'))
print(c(3, 0, '/'))
print(c(3, 2, '%'))
print(c(3, 0, '%'))
print(c(1, 3, 'h'))
