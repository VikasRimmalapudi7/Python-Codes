# return middle eklement in a linked list
class node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class singlee:
    def __init__(self) :
        self.head=None
        self.tail=None
        self.c=0
    def atend(self,value):    #INSERTION AT END
        newnode=node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
           temp=self.head
           while(temp.next):
              temp=temp.next
           temp.next=newnode
    def getmid(self):
        slow,fast=self.head,self.head
        while  fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.value)    

listt=singlee()
listt.atend(1)
listt.atend(2)
listt.atend(3)
listt.atend(4)
listt.atend(5) 
listt.atend(6)
listt.atend(7)       
listt.getmid()

