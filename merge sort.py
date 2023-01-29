def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[0:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        a,b,c=0,0,0
        while a<len(l) and b<len(r):
            if l[a]<r[b]:
                arr[c]=l[a]
                a+=1
            else:
                arr[c]=r[b]
                b+=1
            c+=1
        while a<len(l):
            arr[c]=l[a]
            a+=1
            c+=1
        while b<len(r):
            arr[c]=r[b]
            b+=1
            c+=1
arr= [9,4,8,0,4,6,2,1,0]     
mergesort(arr)
print(arr)
    