n=5
l=[]
for i in range(n):
    l.append([0]*(i+1))
    for j in range(i+1):
        if j==0 or j==i:
            l[i][j]=1
        else:
            l[i][j]=l[i-1][j]+l[i-1][j-1]
print(l)                