class node:                      #Used  to initaialize the node object
 def __init__(self,value):
    self.value=value
    self.next=None
class singlell:
 def __init__(self):
    self.head=None
    self.tail=None
 def atbeg(self,value):      #insertion at beginning
     newnode=node(value)
     newnode.next=self.head
     self.head=newnode
 def  atend(self,value):   #insertion at end
     newnode=node(value)
     if self.head==None:
         self.head=newnode
         return
     else:
         last=self.head
         while(last.next):
             last=last.next
         last.next=newnode    
 def atmid(self,prev,value):  #at mid
     if prev==None:
         print("list is empty")
         return
     else:
         newnode=node(value)
         newnode.next=prev.next
         prev.next=newnode            
 def printlist(self):
     temp=self.head
     while(temp):
         print(temp.value,end="    ")
         temp=temp.next
obj=singlell()
obj.atend(6)
obj.atbeg(5)
obj.atbeg(4)
obj.atend(7)
obj.atmid(obj.head.next,8)
obj.printlist()

