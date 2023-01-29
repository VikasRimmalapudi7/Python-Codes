from collections import deque
de=deque([1,2,3])
de.appendleft(0)
de.extend([5,6,7])
print(len(de))
de=deque(list(map(int,input().split())))
de.extend([1,2,3])
for i in range(len(de)):
    for j in range(i+1,len(de)):
        if de[j]<de[i]:
            de[j],de[i]=de[i],de[j]
