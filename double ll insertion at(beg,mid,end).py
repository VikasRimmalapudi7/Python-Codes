class node:
    def __init__(self,value) :
        self.value=value
        self.next=None
        self.prev=None
class doublell:
    def __init__(self) :
        self.head=None
        self.tail=None
    def  atbeg(self,value):    #AT BEG
        newnode=node(value)
        newnode.next=self.head
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode    
    def  atend(self,value):  #AT END
        newnode=node(value) 
        if self.head==None:
            self.head=newnode
            return
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=newnode
            newnode.prev=last
            return
    def atmid(self,prev,value):    #AT MID
        if prev==None:
            return "it cant't be empty"
        else:
            newnode=node(value)
        newnode.next=prev.next
        prev.next=newnode
        if newnode.next:
            newnode.next.prev=newnode                         
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.value,end="")
            temp=temp.next
obj=doublell()
obj.atend(6)
obj.atbeg(7)
obj.atbeg(1)
obj.atend(4)
obj.atmid(obj.head.next,8)
obj.printlist()