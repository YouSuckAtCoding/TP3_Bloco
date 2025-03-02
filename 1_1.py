from Node import Node

def insert(root, value):

    if root is None:
        return Node(value)

    if root.value == value:
        return root
    elif root.value < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=" ")
        if root.left: preorder(root.left)
        if root.right: preorder(root.right)
    
def postorder(root):
    if root:
        if root.left: postorder(root.left)
        if root.right: postorder(root.right)
        print(root.value, end=" ")

        



r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)
print()
preorder(r)
print()
postorder(r)