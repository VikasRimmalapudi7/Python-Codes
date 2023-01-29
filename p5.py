# reverse a string using stacks

class stack():
     def __init__(self) :
         self.data=[]
         self.data1=[]
     def isempty(self):
         return len(self.data)==0    
     def push(self,v):
         self.data.append(v)
     def pop(self):
         self.data.pop()
     def reverse(self):    
         while(not self.isempty()):
             a=self.data.pop()
             self.data1.append(a)
         return     self.data1
s=stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.push('e')
print(s.reverse())
