class queue:
    def __init__(self,size) :
        self.size=size
        self.list=[]
    def __str__(self):
        vals=[ str(x) for x in self.list]     # The main differnce from stacks and queues are in this str fun() for stacks we use reverse for stacks and for queues we dont use this rev fun().
        return " ".join(vals)
    def isempty(self):  # IS EMPTY
        if self.list==[]:
            return True
        return False
    def enqueue(self,value):   #ENQUEUE
        self.list.append(value)
    def dequeue(self):         #DEQUEUE
        if self.isempty():
            return "not possible"
        else:
           return self.list.pop(0)    
    def isfull(self):         #is full
        if len(self.list)==self.size :
            return "is full" 
        return "not full"
    def peek(self):    #peek
        if self.isempty():
            return "it has no elements"
        else:
            return self.list[0]        
    def delete(self):  #delete
        if self.isempty():
            return "null"
        else:
            self.list=None            
obj=queue(3)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.dequeue()
#obj.delete()
print(obj.isempty())
print(obj.isfull())
print(obj.peek())

