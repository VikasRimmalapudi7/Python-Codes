def quick(arr,low,high):
   if low<high:

    pos=partition(arr,low,high)
    quick(arr,low,pos-1)
    quick(arr,pos+1,high)
def partition(arr,low,high):
    i=low
    j=high-1
    pivot=arr[high]
    while i<j:
        while i<high and arr[i]<pivot:
            i+=1

        while j>low and arr[j]>=pivot:    
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[high]=arr[high],arr[i]
    return i

arr=[99,77,0]   
(quick(arr,0,len(arr)-1))
print(arr)
