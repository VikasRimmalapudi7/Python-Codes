def fun(*nums,**kwargs):
    total=0
    for items in kwargs.values():
        total+=items
    return sum(nums)+total
print(fun(1,2,3,4,5,num1=15,num2=20))    


# ARGS is all about multiple args with only one single name
# KWARGS keyworded args is about under single parameter name wwe can call pass as many as variables into the fun.