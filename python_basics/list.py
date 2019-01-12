my_list = [1, 3, True, 6.5]
print(my_list)

my_list.append("Hello") # Adds a new item to the end of a list
print(my_list)

my_list.insert(2, 'A') # Inserts an item at the ith position in a list
print(my_list)

print(my_list.pop()) # Removes and returns the last element in a list
print(my_list.pop(1)) # Removes and returns the ith element in a list

my_list = [10, 7, -8, 1000, 50]
print("Original list:" ,my_list)
my_list.sort() # Modifies a list to be sorted
print("Oredered list: ", my_list)
my_list.reverse() # Modifies a list to be in reverse order
print("Reversed list: ", my_list)

del my_list[3] # Deletes the item in the ith position
print(my_list)
