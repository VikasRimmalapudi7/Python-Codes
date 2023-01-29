def insertionsort(a):
     for i in range(1,len(a)):
         pos=i
         while (pos>0 and a[pos]<a[pos-1]):
              a[pos],a[pos-1]= a[pos-1],a[pos]
              pos-=1
     return a 
a=[5,1,8,3,9]
print(insertionsort(a))        





 