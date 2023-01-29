#default parameters
def sayhello(name="vikas",emoji="haha"):
    print(f'{name} {emoji}')
sayhello()  
sayhello("michael")  
#positional parameters
sayhello("tyrion","hahahah")
sayhello("eww","jonsnow")
#keyworded args
sayhello(name="damon",emoji="evil")
sayhello(emoji="cute",name="stefan")

# The main diff between functions and methods is,methods are owned by objects whereas functions are only executed whenever they are called.
# when we call method there must be a dot before that method name.
#bt in the case of fun there is no need.