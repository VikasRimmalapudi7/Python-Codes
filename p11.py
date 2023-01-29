class node:
    def __init__(self,value) :
        self.value=value
        self.next=None
        self.prev=None
class double:
    def  __init__(self) :
        self.head=None
        self.tai=None
    def atbeg(self,value):
        newnode=node(value)
        if self.head is None:    
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def atend(self,value):
         newnode=node(value)
         if self.head==None:
             self.head=newnode
         else:
             temp=self.head
             while(temp.next):
                 temp=temp.next 
             newnode.prev=temp
             temp.next=newnode       
    def atmid(self,prev,value):
          newnode=node(value)
          if self.head==None:
             self.head=newnode      
          else:
              temp=self.head
              while(temp.next.value!=prev):
                  temp=temp.next
              nn=temp.next
              temp.next=newnode
              newnode.next=nn
              nn.prev=newnode

    def printing(self):          # TRAVERSING
        temp=self.head
        while(temp):
            print(temp.value,end="  ")
            temp=temp.next        
listt=double()
listt.atbeg(1)
listt.atbeg(2)
listt.atbeg(3)
listt.atbeg(4)
listt.atbeg(5)
listt.atend(99)
listt.atend(199)
listt.atend(299)
listt.atmid(1,333)
listt.printing()



         
        