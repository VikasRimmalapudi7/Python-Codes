a=list(map(int,input().split()))
b=list(map(int,input().split()))
i,j=0,len(b)-1
l=[]
while ( len(a)>0 and len(b)>0  and j>=0):
    if a[i]<b[j]:
        a.remove(a[i])
        l.append(2)
    elif a[i]>b[j]:
        b.remove(b[j])
        l.append(1)
        j-=1
    else:
        a.remove(a[i])
        b.remove(b[j])
        l.append(0)
        j-=1
print(l)        


