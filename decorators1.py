from time import time
def fun1(fun):
    def wrap(*args,**kwargs):
        t1=time()
        result=fun(*args,**kwargs)
        t2=time()
        print(f'it took {t2-t1} s')
        return result
    return wrap
@fun1
def fun():
    for i in range(100000000):
        i*5
fun()        

