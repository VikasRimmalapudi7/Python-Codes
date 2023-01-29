def selectionsort(a):
   for i in range(len(a)):
       minpos=i
       for j in range(i+1,len(a)):
           if a[minpos]>a[j]:
               minpos=j
       a[i],a[minpos]=a[minpos],a[i]       
   return a    
       
a=[5,3,6,9,1,2]
print(selectionsort(a))
