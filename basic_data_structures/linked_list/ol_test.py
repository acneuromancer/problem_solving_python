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

ol.add(0)
print_list(ol)

print('Size of the list: %d' % ol.size())

print('Removing 5 from the list: %s' % ol.remove(5))
print_list(ol)

for i in range(-1, 12):
    print('Is %d in the list? %s' % (i, ol.search(i)))

print('Is 300 in the list? %s' % ol.search(300))
