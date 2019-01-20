class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [[] for i in range(self.size)]
        self.data = [[] for i in range(self.size)]

    def hash_function(self, key, size):
        return key % size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)
        self.slots[hash_value].append(key)
        self.data[hash_value].append(data)

    def get(self, key):
        hash_value = self.hash_function(key, self.size)

        i = 0
        found = False
        while i < len(self.slots[hash_value]) and not found:
            if self.slots[hash_value][i] == key:
                found = True
            else:
                i += 1

        if found:
            return self.data[hash_value][i]
        else:
            return None

    def delete(self, key):
        hash_value = self.hash_function(key, self.size)

        i = 0
        found = False
        while i < len(self.slots[hash_value]) and not found:
            if self.slots[hash_value][i] == key:
                found = True
            else:
                i += 1

        if not found:
            return None

        del self.slots[hash_value][i]
        del self.data[hash_value][i]

    def display(self):
        print(self.slots)
        print(self.data)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable()
h.put(1, "Apple")
h.put(100, "Pear")
h.put(5, "Melon")
h.display()

print(h.get(100))
print(h.get(5))
print(h[1])
print(h[30])

h.delete(500)
h.display()
