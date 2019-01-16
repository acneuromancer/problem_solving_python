from UnorderedList import UnorderedList

def print_list(ul):
    node = ul.head

    while node != None:
        print(node.get_data(), end=" ")
        node = node.get_next()

    print()


l = UnorderedList()

for i in range(10):
    l.append(i)

print_list(l)

l.add(-1000)
l.append(-3000)
print_list(l)

# l.remove(-10)
l.remove(-1000)
print_list(l)

l.remove(-3000)
print_list(l)

print(l.remove(5))
print_list(l)

print(l.remove(-101))
