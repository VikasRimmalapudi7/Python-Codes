class Node:
    def __init__(self,value) :
        self.left=None
        self.right=None
        self.value=value
    def insert(self,val):
       if self.value: 
          if val<self.value:
            if self.left is None:
                self.left=Node(val)
            else:
                self.left.insert(val) 
          elif val>self.value:
            if self.right is None:
                self.right=Node(val)
            else:
                self.right.insert(val)
       else:
           self.value=val

    def printtree(self):
          if self.left:
              self.left.printtree()
          print(self.value)
          if self.right:
              self.right.printtree()
    def inorder(self,root):
        res=[]
        if root:
            res=self.inorder(root.left)        
            res.append(root.value)
            res=res+self.inorder(root.right)
        return res     
    def preorder(self,root):
        res=[]
        if root:
            res.append(root.value)
            res+=self.preorder(root.left)        
            res=res+self.preorder(root.right)
        return res     
    def postorder(self,root):
        res=[]
        if root:
            res=self.postorder(root.left)        
            res=res+self.postorder(root.right)
            res.append(root.value)
        return res              
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorder(root))
print(root.preorder(root))
print(root.postorder(root))