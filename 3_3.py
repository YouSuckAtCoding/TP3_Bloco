#!usr/bin/env python3
from multiprocessing.pool import ThreadPool
from Node import Node
from collections import deque
from multiprocessing import Value

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

def inorderMax(root, max):

    if root:
        
        res = root.value
        lres = inorderMax(root.left, max)        
        rres = inorderMax(root.right, max)        

        if res < lres:
            res = lres
        elif res < rres:
            res = rres

        max.value = res
        return res
    
    else:
        return float('-inf')

def parallel_max(root):
      
    resAggr = Value('i', -9999999)
    with ThreadPool(2) as pool:
        pool.starmap(inorderMax, [(root.left, resAggr), (root.right, resAggr)])

    return resAggr.value

if __name__ == '__main__':

   root = Node(10)

   insert(root, 20)
   insert(root, 30)
   insert(root, 40)
   insert(root, 50)
   insert(root, 60)

   inorder(root)
   print("max : ", parallel_max(root))