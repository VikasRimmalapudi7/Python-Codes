class mygen:
 cur=0
 def __init__(self,first,last):
    self.first=first
    self.last=last
 def __iter__(self):
     return self
 def __next__(self):
     if mygen.cur<self.last:
         num=mygen.cur
         mygen.cur+=1
         return num
     raise StopIteration    
obj=mygen(0,10)
for i in obj:
    print(i)     
#############
def fun(nums):
    for i in  range(nums):
        yield i**2
ab=fun(10)
for i  in ab:
    print(i)        
    # GENERATORS consists of both iterartors
    #here yield is used to pAause the function until next is called .
    


