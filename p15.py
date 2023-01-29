def fun(num):
    s=0
    n=0
    while(num>0):
        temp=num%10
        s+=temp
        num=num//10
    while(s!=0) :
        temp1=s%10
        n+=temp1
        s//=10
    print(n)    

num=int(input("enter num"))
fun(num)