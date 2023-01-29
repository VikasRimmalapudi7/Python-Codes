import threading
def cube(num):
    print(num**3)
def sq(num):
    print(num**2)
t1,t2=threading.Thread(target=cube,args=(10,)),threading.Thread(target=sq,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
