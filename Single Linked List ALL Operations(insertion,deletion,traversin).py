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
        else:    
         newnode.next=self.head
         self.head=newnode         
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
    def atmid(self,prev,value):  #INSERTION AT specific pos
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
    def printing(self):          # TRAVERSING
        temp=self.head
        while(temp):
            print(temp.value,end="  ")
            temp=temp.next
    def delbeg(self):            # DELETION AT BEGINNING
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None    
    def delend(self):            # DELETION AT END
        if self.head==None:
            print("list is empty")
        else:
            cur=None
            temp=self.head
            while temp.next:
                cur=temp
                temp=temp.next
            cur.next=None
    def delmid(self,value):         # DELETION AT MID
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
listt.atmid(3,99)
listt.atmid(4,109)
listt.printing()



            
        