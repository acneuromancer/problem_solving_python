from BinaryTree import BinaryTree

r = BinaryTree('a')
print(r.get_root_val())
#print(r.get_left_child())

r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())

r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())

r.get_right_child().set_root_val('hello')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
