"""class a:
    num=10
class b(a):                                   #here in mro first the D class checks the C class and then B class then after it checks the A class.   
                                              #thats why it prints num as 1 so its called as method resolutio order
    num=9
class c(a):
    pass
class d(c,b):
    pass
obj=d()
print(obj.num)    """
class a:
    pass
class b:
    pass
class c:
    pass
class x(a,b):
    pass
class y(b,c):
    pass
class m(x,y,c):
    pass
print(m.__mro__)
