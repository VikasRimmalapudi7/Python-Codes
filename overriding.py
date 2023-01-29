class a:
    def fun(self):
        print("hi")
class b(a):
    def fun(self):
        super().fun()
        print("bye")

obj=b()
obj.fun()                