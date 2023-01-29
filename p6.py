# to make string great
s="AaBbbCCc"
res=[]
for i in range(len(s)):
    oc=s[i].swapcase()
    if len(res)==0:
        res.append(s[i])
    elif res[-1]==oc:
        res.pop()
    else:
        res.append(s[i])
print("".join(res))    
