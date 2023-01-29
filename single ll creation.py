class node:
 def __init__(self,value=None):
    self.value=value
    self.next=None
class singlell:
 def __init__(self):
    self.head=None
    self.tail=None
ss=singlell()
temp1=node(10)
temp2=node(20)
ss.head=temp1
ss.head.next=temp2
ss.tail=temp2
def __iter__(self):
    node=self.head
    while node:
        yield node
        node=node.next




