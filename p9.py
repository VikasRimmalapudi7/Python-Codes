class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class single:
    def __init__(self) :
        self.head=None
        self.tail=None
    def atbeg(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode   
        newnode.next=self.head
        self.head=newnode     
    def atend(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode   
            return
        else:
           temp=self.head 
           while(temp.next):
              temp=temp.next
           temp.next=newnode
    def atmid(self,prev,value):
        if prev==None:
            print("list is empty")
        else:
            newnode=node(value)
            newnode.next=prev.next
            prev.next=newnode
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.value,end=" ")
            temp=temp.next
listt=single()
listt.atend(1)
listt.atend(2)
listt.atend(3)
listt.atend(4)
listt.atend(5)
listt.atbeg(6)
listt.atbeg(7)
listt.atbeg(8)
listt.atmid(listt.head.next.next,99)
listt.atmid(listt.head.next.next,101)
listt.atmid(listt.head.next.next.next,103)
listt.printing()
                
        
