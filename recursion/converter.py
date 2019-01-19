class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def to_str(n, base):

    r_stack = Stack()
    convert_string = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])

        n = n // base

    result = ""

    while not r_stack.is_empty():
        result += str(r_stack.pop())

    return result


print(to_str(255, 2))
print(to_str(526, 2))
print(to_str(65535, 16))
