def dec(func):
    def greet(*x,**y):
        print("hi vikas")
        func(*x,**y)
        print("bye vikas")
    return greet
@dec    
def hello(parameter,parameter2):
    print(parameter,parameter2)    
hello("vikas","rimmalapudi") 