s="qwerty@821142"
l=[]
for c in s:
    if c.isdigit():
        l.append((c))
lt=(list(set(l)))
lt.sort()
a=lt[::-1]
siz=len(a)
for i in range(siz-1,0,-1):
        
        if int(a[i])%2==0:
            t=a[i]
            a.remove(a[i])
            a.insert(siz-1,t)
        num=int("".join(a))
        if num%2==0:
             print(num)
             break
else:
    print(-1)
        
