#!usr/bin/env python3
from Node import Node



def insert(root, value):
    if root is None:
        return Node(value)

    if root.value == value:
        return root

    if root.value < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root



def search(root , key):

    if root is None or root.value == key:
        return root

    elif root.value < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

nums = [50, 30, 70, 20, 40, 60, 80]

root = Node(nums[0])

for i in range(1, len(nums)):
    root = insert(root, nums[i])
    
inorder(root)
print()
if search(root, 40) : print("Encontrado") 
else: print("Não encontrado")