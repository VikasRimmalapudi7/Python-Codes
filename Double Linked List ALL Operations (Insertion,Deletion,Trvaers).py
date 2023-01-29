class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class doub:
    def __init__(self) :
        self.head=None
        self.tail=None
    def atbeg(self,value):
        newnode=node(value)
        if self.head is None:
              self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def atend(self,value):
        newnode=node(value)
        if self.head is None:
              self.head=newnode  
        else:
            temp=self.head
            while  temp.next:
                temp=temp.next
            newnode.prev=temp    
            temp.next=newnode  

    def atmid(self,prev,value):
        newnode=node(value)
        if self.head is None:
              self.head=newnode  
        else:
            temp=self.head
            while temp.next.value!=prev:
                temp=temp.next
            nn=temp.next
            newnode.next=nn
            temp.next=newnode
            newnode.prev=temp
            nn.prev=newnode

    def delbeg(self):
        if not self.head:
            return "not possible"
        else:
            temp=self.head
            self.head=temp.next
            temp=None
            self.head.prev=None

    def delend(self):
        temp=self.head
        cur=None
        while temp.next:
            cur=temp
            temp=temp.next
        cur.next=None
        temp=None    


    def delmid(self,prev):
        if not self.head:
            return "not possible"
        else:
            temp=self.head
            cur=None
            while temp.value!=prev:
                cur=temp
                temp=temp.next
            cur.next=temp.next
            temp.next.prev=cur    
    def printing(self):
        temp=self.head
        while temp:
            print(temp.value,end=' ')
            temp=temp.next

obj=doub()
obj.atbeg(3) 
obj.atbeg(2)                             
obj.atbeg(1)
obj.atend(4)
obj.atend(5)
obj.atmid(3,99)
obj.atmid(4,109)
obj.delbeg()
obj.delend()
obj.delmid(3)
obj.printing()
            
        