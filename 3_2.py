#!usr/bin/env python3
from Node import Node
from collections import deque
from multiprocessing import Process

def insert(root, value):

    if root is None:
        root = Node(value)
        return root

    q = deque()
    q.append(root)
        
    while q:

        curr = q.popleft()

        if curr.left is None:
            curr.left = Node(value)
            return root
        else:
            q.append(curr.left)
        
        if curr.right is None:
           curr.right = Node(value)
           return root
        else:
            q.append(curr.right)
              

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def inorderSearch(root, value, path=[]):
    if root:
        path.append(root.value)

        if root.value == value:
            print(path)
       
        inorderSearch(root.left, value, path)
        inorderSearch(root.right, value, path)        

def parallel_search(root, target):

    if root.value == target:
        return target
    
    left_proc = Process(target=inorderSearch, args=(root.left, target, [root.value]))
    right_proc = Process(target=inorderSearch, args=(root.right, target, [root.value]))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()


if __name__ == '__main__':

   root = Node(10)

   insert(root, 20)
   insert(root, 30)
   insert(root, 40)
   insert(root, 50)
   insert(root, 60)

   inorder(root)
   parallel_search(root, 20)