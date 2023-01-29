def fun():
    x="vikas"
    def fun1():
        nonlocal x
        x="rimmalapudi"
        print(x)
    fun1()
    print(x)
fun()        
# Here NON LOCAL keyword is all about when u assign a valuee to the  variable which is declared as non loacl then its values
 #doesnt change even in the outside of the function 