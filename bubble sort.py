def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
a=[99,10,88,34,22,1,90,99,79]
bubble(a)

