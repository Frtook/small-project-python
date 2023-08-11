class stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def puch(self, value):
        self.item.append(value)

    def top(self):
        if self.is_empty() == False:
            return self.item[-1]

    def pop(self):
        if self.is_empty() == False:
            return self.item.pop()


def pr(o):
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "^":
        return 3
    else:
        return 0


def eva(value):
    R = []
    s = stack()
    n = ""
    if value.count("(") != value.count(")"):
        raise Exception("Error '(' != ')' !!!")
    for i in value:
        if i == " ":
            continue
        if i == '(':
            s.puch(i)
        elif i == ")":
            if n != "":
                R.append(n)
                n = ""
            while s.top() != "(":
                R.append(s.pop())
            s.pop()
        elif i == "+" or i == "-" or i == "*" or i == "/" or i == "^":
            if n != "":
                R.append(n)
                n = ""
            if len(s.item) > 0:
                while pr(s.top()) >= pr(i):
                    R.append(s.pop())
                    if len(s.item) == 0:
                        break
            s.puch(i)
        else:
            n += i
    if n != "":
        R.append(n)

    while len(s.item) != 0:
        R.append(s.pop())

    ##print(R)
    for i in R[::]:
        if i == "+":
            n1 = R[R.index("+") - 2]
            n2 = R[R.index("+") - 1]
            R.remove(R[R.index("+") - 2])
            R.remove(R[R.index("+") - 1])
            c = float(n1) + float(n2)
            R.insert(R.index("+"), c)
            R.remove("+")
        elif i == "*":
            n1 = R[R.index("*") - 2]
            n2 = R[R.index("*") - 1]
            R.remove(R[R.index("*") - 2])
            R.remove(R[R.index("*") - 1])
            c = float(n1) * float(n2)
            R.insert(R.index("*"), c)
            R.remove("*")
        elif i == "-":
            n1 = R[R.index("-") - 2]
            n2 = R[R.index("-") - 1]
            R.remove(R[R.index("-") - 2])
            R.remove(R[R.index("-") - 1])
            c = float(n1) - float(n2)
            R.insert(R.index("-"), c)
            R.remove("-")
        elif i == "/":
            n1 = R[R.index("/") - 2]
            n2 = R[R.index("/") - 1]
            R.remove(R[R.index("/") - 2])
            R.remove(R[R.index("/") - 1])
            c = float(n1) / float(n2)
            R.insert(R.index("/"), c)
            R.remove("/")
        elif i == "^":
            n1 = R[R.index("^") - 2]
            n2 = R[R.index("^") - 1]
            R.remove(R[R.index("^") - 2])
            R.remove(R[R.index("^") - 1])
            c = float(n1) ** float(n2)
            R.insert(R.index("^"), c)
            R.remove("^")
    return float(R[0])


result = eva(input("Enter Eq.. :"))

print(result)
