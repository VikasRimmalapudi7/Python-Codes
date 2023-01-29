class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
   if root: 
    inorder(root.left)
    print(root.val,end="")
    inorder(root.right)
def postorder(root):
  if root:  
    inorder(root.left)
    inorder(root.right)
    print(root.val,end="")
def preorder(root):
   if root: 
    print(root.val,end="")
    inorder(root.left)
    inorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print(inorder(root))
print(preorder(root))
print(postorder(root))