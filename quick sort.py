def quicksort(a,low,high):
    if low<high:
        pos=partition(a,low,high)
        quicksort(a,low,pos-1)
        quicksort(a,pos+1,high)
def partition(a,low,high):
    i=low
    j=high-1
    pivot=a[high]
    while i<j:
        while i<high and a[i]<pivot:
            i+=1
        while j>low and a[j]>=pivot:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    if a[i]>pivot:
        a[i],a[high]=a[high],a[i]
    return i
arr=[21,5,30,10,11,92,67,23]
quicksort(arr,0,len(arr)-1)
print(arr)            

