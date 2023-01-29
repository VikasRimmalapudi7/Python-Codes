class user:
    def fun(self):
        print("hello there")
class laptop(user):
    def __init__(self,name,model) :
        self.name=name
        self.model=model
    def features(self):
        print(f'{self.name} has very best feature and its model is {self.model}')
class comp(user):
    def __init__(self,name,mouse):
        self.name=name
        self.mouse=mouse
    def work(self):
        print(f'{self.name} consists of {self.mouse}')
class Net(laptop,comp):    
        def __init__(self, name, model,mouse):     # in this line bcoz of multiple inheritance we should define init method that contains all the variabls 
            laptop.__init__(self,name,model)    #in this line we have to declare the class name dot init method that consists of  attributes
            comp.__init__(self,name,mouse)      # same as above line
obj=Net("lenovo","idaepad 5","hp")
print(obj.features())
print(obj.fun())
            