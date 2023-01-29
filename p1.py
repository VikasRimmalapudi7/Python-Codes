n=int(input())
x=[]
for i in range(n):
   x.append(list(map(int,input().split())))
c=0
sum1=sum(x[0])
for i in range(1,n):
    if sum1<sum(x[i]):
        c+=1   
print(c)