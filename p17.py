def bin(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==key:
            return mid
        elif a[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
print(bin(arr,40))                

