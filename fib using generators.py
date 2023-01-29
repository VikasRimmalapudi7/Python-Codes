# in this prog we are printing some number of fibonacci numbers
def fibonacci(num):
    a=1
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b=temp+b
obj=fibonacci(10)        
for i in obj:
    print(i)