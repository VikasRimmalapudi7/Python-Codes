class a:
    def __init__(self,name):
        self.name=name
class b(a):
    def __init__(self,name,num,num2) :
        self.name=name
        self.num=num
        self.num2=num2
        super().__init__(name)
obj=b("vikas",6,7)
print(obj.name)        
