class Stack:
    def __init__(self,size) :    #Creation of stack
        self.size=size
        self.list=[]
    def push(self,value):       #PUSH
        self.list.append(value)
    def isempty(self):          #IS EMPTY
        if len(self.list)==0:
            return True
        return False
    def pop(self):              #POP
        if self.isempty():
            return "stack is empty"
        self.list.pop()  
    def isfull(self):           #ISFULL
        if len(self.list)==self.size:
            return True
        return False    
     
    def peek(self):   #PEEK
         return self.list[len(self.list)-1]
    def delete(self):
        self.list=None
obj=Stack(3)
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()

print(obj.peek())
print(obj.isfull())
print(obj.isempty())
#obj.delete()    #it is used when there is no str() method....
print(obj) 

 

        