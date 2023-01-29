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
           self.value=Node(val)

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

    def inorder_iteratively(self,root):
        res=[]
        stack=[]
        cur=root
        while True:
            if cur:
                stack.append(cur)
                cur=cur.left
            elif stack:
                 cur=stack.pop()
                 res.append(cur.value)
                 cur=cur.right
            else:
                break
        return res             
    def preorder_iterative(self,root):
        stack=[]
        stack.append(root)
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res    
    def postorder_iterative(self,root):
        stack=[]
        res=[]
        cur=root
        while True:
            while root:
                if root.right:
                   stack.append(root.right)
                stack.append(root)
                root=root.left
            root=stack.pop()
            s=stack[-1] if stack else None
            if root.right and s==root.right:
                stack.pop()
                stack.append(root)
                root=root.right
            else:
                res.append(root.value)
                root=None
            if not stack:
                return res    
    def preorder(self,root):
        res=[]
        if root:
            res.append(root.value)
            res=res+self.preorder(root.left)        
            res=res+self.preorder(root.right)
        return res     
    def postorder(self,root):
        res=[]
        if root:
            res=self.postorder(root.left)        
            res=res+self.postorder(root.right)
            res.append(root.value)
        return res     
    def deleteNode(self,root,key):
        if not root:
            return root
        if  key<root.value:
            root.left=self.deleteNode(root.left,key)
        elif  key>root.value:
            root.right=self.deleteNode(root.right,key) 
        else:
            #here is the matching node
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            #if 2 childs then in order succesor
            temp=root.right
            while temp.left:
                temp=temp.left
            root.value=temp.value    
            root.right=self.deleteNode(root.right,temp.value)
        return root
root = Node(20)
root.insert(-3)
root.insert(-10)
root.insert(5)
root.insert(9)
print(root.inorder(root))
print(root.inorder_iteratively(root))

print(root.preorder(root))
print(root.preorder_iterative(root))

print(root.postorder(root))
print(root.postorder_iterative(root))