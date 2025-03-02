from Node import Node
from multiprocessing import Process, Value
from collections import deque

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

def search_subtree(node, target, found):
   
   if node is None or found.value:
       return
   if node.value == target:
       found.value = True
       return
   
   search_subtree(node.left, target, found)
   search_subtree(node.right, target, found)

def parallel_search(root, target):
    
    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()

    return found.value

if __name__ == '__main__':

   root = Node(10)

   insert(root, 20)
   insert(root, 30)
   insert(root, 40)
   insert(root, 50)
   insert(root, 60)

   print(f"Valor 60 encontrado: {bool(parallel_search(root, 60))}")
   print(f"Valor 75 encontrado: {bool(parallel_search(root, 75))}")