from OrderedList import OrderedList

def print_list(ol):
    current = ol.head

    while current != None:
        print(current.get_data(), end=" ")
        current = current.get_next()

    print()


ol = OrderedList()
for i in range(10, 0, -1):
    ol.add(i)

print_list(ol)

ol.add(-1000)
print_list(ol)

ol2 = OrderedList()
print(ol2)
