class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def len(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return "is Empty"
        else:
            return self.items.pop(0)

    def first(self):
        if self.is_empty():
            return "is empty"
        else:
            return self.items[0]

    def last(self):
        if self.is_empty():
            return "is empty"
        else:
            return self.items[-1]


class stack:
    def __init__(self) -> None:
        self.item = []

    def push(self, val):
        self.item.append(val)

    def is_empty(self):
        return len(self.item) == 0

    def pop(self):
        if not self.is_empty():
            self.item.pop()
        else:
            print("is empty")

    def len(self):
        return len(self.item)

    def top(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            print("is empty")


# q = queue()
#
# import collections
#
# d = collections.deque()
# d.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(q)
#
# q = queue()
# q2 = queue()
# for i in range(11, 19):
#     q.enqueue(i)
# s = stack()
# for i in q.items:
#     if i == q.items[len(q.items) // 2]:
#         break
#     else:
#         s.push(q.dequeue())
# for i in range(len(s.item)):
#     q2.enqueue(s.item[i])
#     q2.enqueue(q.items[i])
# print(s.item)
# print(q.items)
# print(q2.items)
#
# s = stack()
# q = queue()
# for i in range(11, 19):
#     s.push(i)
#
# print(s.item)
#
# for i in range(len(s.item) // 2):
#     q.enqueue(s.item[i])
#     q.enqueue(s.top())
#
# print(q.items)
