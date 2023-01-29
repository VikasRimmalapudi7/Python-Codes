class stack():
    def __init__(self,size) :
        self.data=[]
        self.size=size
    def isempty(self):
        return (len(self.data)==0)

    def push(self,v):
        if self.isfull():
            return "its full"
        self.data.append(v)

    def isfull(self):
        return len(self.data)==self.size

    def pop(self):
        if self.isempty():
            print("stack is empty")
        self.data.pop()
        
    def iter(self):
        for i in self.data:
            print(i,end="   ") 

obj=stack(5)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)

obj.pop()
obj.pop()
print(obj.isfull())
print(obj.isempty())
obj.iter()






        