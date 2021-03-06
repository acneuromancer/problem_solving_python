from Node import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, value):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == value:
                found = True
            current = current.get_next()

        return found

    def append(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
            return

        current = self.head
        while current.get_next() != None:
            current = current.get_next()

        current.set_next(temp)

    def remove(self, value):
        current = self.head
        previous = None
        found = False

        while not found and current != None:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            return False

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return True
