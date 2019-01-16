from Node import Node

class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        stop = False
        found = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            return False

        if previous == None:
            self.head = current.get_next()
            return True

        previous.set_next(current.get_next())
        return True

    def search(self, item):
        current = self.head
        stop = False
        found = False

        while current != None and not stop and not found:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()

        return found
