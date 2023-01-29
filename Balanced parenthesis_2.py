def minswaps(s):
    if len(s)%2!=0:
        return -1
    l=r=0
    for i in range(len(s)):
        if s[i] == ")":
            if l==0:
                r+=1
            else:
                l-=1
        else:
            l+=1
    if l%2==0:
        return l
    else:
        return (l+1)//2
s="()())("
print(minswaps(s))                    

            











