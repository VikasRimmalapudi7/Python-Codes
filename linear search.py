def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return "found at",i
    return -1
arr=[1,2,3,4,5,6,7,8]
print(linear_search(arr,4))        