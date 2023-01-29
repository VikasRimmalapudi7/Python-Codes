class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def insert(self,data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printing(self):
            if self.left:
                self.left.printing()
            print(self.data)
            if self.right:
                self.right.printing()
root=Node(12)
root.insert(6)
root.insert(3)
root.insert(14)
root.printing()

