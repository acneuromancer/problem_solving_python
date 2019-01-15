from Deque import Deque

d = Deque()

print(d.is_empty())

d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)

print(d.size())
print(d.remove_rear())
print(d.remove_front())
