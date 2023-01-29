class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None

        
class circle:
    
    def __init__(self):
      self.head = None


    def add_data(self,value) :  #at beg
        newnode=Node(value)
        temp=self.head
        newnode.next=temp
        if self.head is not None:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            
        else:
            newnode.next=newnode
        self.head=newnode
   
    def atend(self,value) :  #at end
        newnode=Node(value)
        if(self.head == None):
            self.head = newnode
            newnode.next = self.head
            return
        else:
    
    #5. Else, traverse to the last node
               temp = self.head
               while(temp.next != self.head):
                     temp = temp.next
    
    #6. Adjust the links  
               temp.next = newnode
               newnode.next = self.head
    def atmid(self,prev,value):  #INSERTION AT specific pos
          newnode=Node(value)
          if self.head==None:
             newnode.next=newnode
             self.head=newnode      
          else:
              temp=self.head
              while(temp.next.value!=prev):
                  temp=temp.next
              nn=temp.next
              temp.next=newnode
              newnode.next=nn    
            
    def delend(self):
        temp=self.head
        if not self.head:
            return 'None'
        else:
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next=None

    def delbeg(self):
        cur=self.head.next
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=cur
        self.head=cur    

    def delmid(self,val):
        if self.head is None:
            return
        else:
            cur=None
            temp=self.head
            while(temp.value != val):
             cur=temp
             temp=temp.next
            cur.next=temp.next
            temp=None


        


    
    def printing(self):
        temp=self.head
        while temp:
            print(temp.value,end='  ')
            temp=temp.next
            if temp==self.head:
                break
obj=circle()
obj.add_data(5)
obj.add_data(4)
obj.add_data(3)
obj.add_data(2)
obj.add_data(1)
obj.atmid(3,99)
obj.atend(101)
obj.delbeg()
obj.delmid(3)
obj.delend()
obj.printing()                



