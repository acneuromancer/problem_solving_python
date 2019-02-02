class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0


    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]

            i //= 2


    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)


    def perc_down(self, i):
        while i*2 <= self.current_size:
            mc = self.min_child(i)

            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]

            i = mc


    def min_child(self, i):
        if i*2 + 1 > self.current_size:
            return i * 2
        elif:
            self.heap_list[i*2] < self.heap_list[i*2 + 1]:
            return i * 2
        else:
            return i * 2 + 1
