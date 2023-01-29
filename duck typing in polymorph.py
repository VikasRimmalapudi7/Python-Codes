class java:
    def code(self):
        print("in this java is running")
class python:
    def code(self):
        print("py is running")        
class lap:
    def hacky(self,xoxo):
        print("they are working in laptop")
        xoxo.code()
obj=java()
obj1=python()
obj2=lap()
obj2.hacky(obj)                
#DUCK TYPING :-it is all about when u have 2 classes with same method names and another class calling that fun now it all depends on which class object are we passing \
#into the class object i.e hacky
