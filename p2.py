def mergesort(arr):
 if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        a,b,c=0,0,0
        while a<len(left) and b<len(right):    
         if left[a]<right[b]:
            arr[c]=left[a]
            a+=1
         elif left[a]>right[b]:
            arr[c]=right[b]
            b+=1
         c+=1
        while a<len(left):
            arr[c]=left[a]
            a+=1
            c+=1
        while b<len(right):
            arr[c]=right[b]
            b+=1
            c+=1    
        return arr    
arr=[3,5,1,2,99,109,22]
print(mergesort(arr))