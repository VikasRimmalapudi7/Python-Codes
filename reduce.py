from functools import*
mylist=[1,2,3,1,1,1,1]
def acc(a,item):
    print(a,item)
    return a+item
print(reduce(acc,mylist))    