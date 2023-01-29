def mergesort(a,b):
    c=[]
    m=len(a)
    n=len(b)
    i,j=0,0
    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j+=1
        elif j==n:
            c.append(a[i])
            i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j] :
            c.append(b[j])
            j+=1
    return c
a=[1,3,5,7] 
b=[0,2,4,6,8,9]
print(mergesort(a,b))                  
