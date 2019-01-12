from Stack import Stack

s = Stack()
print('\nInitial size of the stack: ', s.size())

print('\nTest whether the stack is empty: ', s.is_empty())

s.push("Apple")
s.push(True)
s.push(6.31448)
s.push(10)

print('\nPeek into the stack: ', s.peek())

print('\nSize of the stack: ', s.size())

print('\nPop all items from the stack:')
while not s.is_empty():
    print(s.pop(), end=" ")
print()
