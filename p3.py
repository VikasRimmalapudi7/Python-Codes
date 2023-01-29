# return the min element in stack using stack operations?
class stack():
    def __init__(self) :
        self.data=[]
    def isempty(self):
        return (len(self.data)==0)    
    def push(self,v):
        self.data.append(v)
    def pop(self):
        self.data.pop()
    def getMin(self):
        a=self.data.pop()
        while(not self.isempty()):
            b=self.data.pop()
            if a>b:
                a=b
        return "the min element is:",a
s=stack()
t=int(input("enter no of test  cases"))
while(t):
    n=int(input("enter no of elements"))
    print("enter numbers")
    for i in range(n):
        s.push(int(input()))
    t-=1
print(s.getMin())
    



