#!usr/bin/env python3
from Node import Node

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


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


def deleteNode(root, x):
    
    if root is None: 
       return root 
    
    if root.value > x:
       root.left = deleteNode(root.left, x)
    elif root.value < x:
       root.right = deleteNode(root.right, x)
    
    else:

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:

            succ = get_successor(root)
            root.value = succ.value
            root.right = deleteNode(root.right, succ.value)
        
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

nums = [50, 30, 70, 20, 40, 60, 80]

root = Node(nums[0])

for i in range(1, len(nums) - 1):
    root = insert(root, nums[i])

print(inorder(root))
deleteNode(root, 20)
print(inorder(root))
deleteNode(root, 30)
print(inorder(root))
deleteNode(root, 50)
print(inorder(root))