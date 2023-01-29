class node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class singlee:
    def __init__(self) :
        self.head=None
        self.tail=None
    def atbeg(self,value):    # INSERTION AT BEGINNING
        newnode=node(value)
        if self.head==None:
            self.head=newnode   
        newnode.next=self.head
        self.head=newnode
    def middle(self):             
      slow=fast=self.head  
      while fast and fast.next:
          slow=slow.next
          fast=fast.next.next
      print (slow)
listt=singlee()
listt.atbeg(1)
listt.atbeg(2)
listt.atbeg(3)
listt.atbeg(4)
listt.atbeg(5) 
listt.atbeg(6)
listt.atbeg(7)   
listt.middle()
      