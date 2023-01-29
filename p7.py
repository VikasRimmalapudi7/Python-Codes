# to remove adjacent duplicates
s="AaBbbCCc"
res=[]
for i in range(len(s)):
    if len(res)==0:
        res.append(s[i])
    elif res[-1]==s[i]:
        res.pop()
    else:
        res.append(s[i])
print("".join(res))    
