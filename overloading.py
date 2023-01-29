class lap:
    def add(self,a,b,c):
        if c>0:
            print(a+b+c)
        else:
            print(a+b)
obj=lap()
obj.add(10,20,0)           
# in python method overloading is nopt exactly supported we have to make some minor changes in the methods