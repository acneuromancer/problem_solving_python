"""
Completed implementation of a deque abstract data class

Deque() - creates a new deque that is empty. It needs no parameters and returns an empty deque.

add_fron(item) - adds a new item to the front of the deque. It needs the item and returns nothing.

add_rear(item) - adds a new item tho the rear of the deque. It needs the item and returns nothing.

remove_front() - removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

remove_rear() - removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

is_empty() - tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

size() - returns the number of items in the deque. It needs no parameters and returns an integer.
"""

class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
