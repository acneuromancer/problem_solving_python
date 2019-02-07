from TreeNode import TreeNode
from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()
bst.put(10, 'A')
bst.put(1, 'B')
bst.put(11, 'C')
bst[20] = 'D'

print(bst.get(10))
print(bst[11])
print(bst.get(-1))
print(10 in bst)

bst["A"] = 20
print(bst["A"])
