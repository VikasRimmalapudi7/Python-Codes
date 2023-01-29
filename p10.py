class node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class singlee:
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
    def atmid(self,prev,value):  #at mid
     if prev==None:
         print("list is empty")
         return
     else:
         newnode=node(value)
         newnode.next=prev.next
         prev.next=newnode                   
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.value,end="  ")
            temp=temp.next
    def delbeg(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None    
    def delend(self):
        if self.head==None:
            print("list is empty")
        else:
            cur=None
            temp=self.head
            while temp.next:
                cur=temp
                temp=temp.next
            cur.next=None
    def delmid(self,value):
        cur=None
        temp=self.head
        while(temp.value != value):
            cur=temp
            temp=temp.next
        cur.next=temp.next
        temp=None




listt=singlee()
listt.atend(1)
listt.atend(2)
listt.atend(3)
listt.atend(4)
listt.atend(5) 
listt.atend(6)
listt.atend(7)   
listt.delbeg()  
listt.delend()
listt.delmid(4)
listt.printing()



            
        