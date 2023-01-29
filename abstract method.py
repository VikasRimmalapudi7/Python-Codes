from abc import ABC,abstractmethod
class comp(ABC):
    @abstractmethod
    def process(self):
        pass
class lap(comp):
    def process(self) :
        print("its working")
class board(lap):
    def write(self):
        print("its writing")
class phone(board):
    def code(self,a):
        print("gaming phone")
        a.process()        
obj1=board()
obj=phone()
obj.code(obj1)
           