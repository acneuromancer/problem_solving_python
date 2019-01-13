from Queue import Queue

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print("Size of the queue is %d." % q.size())

while not q.is_empty():
    print(q.dequeue(), end = " ")

print()
