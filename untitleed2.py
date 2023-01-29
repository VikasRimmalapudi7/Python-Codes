p=[0,1,2,5,6]
wt=[0,2,3,4,5]
m=8
n=len(p)
k=[[0 for i in range(m+1)] for  j in range(n+1)]
for i in range(n+1):
    for w in range(m+1):
        if i==0 or w==0:
            k[i][w]=0
        elif wt[i-1]<=w:
            k[i][w]=max((p[i-1]+k[i-1][w-wt[i-1]]),k[i-1][w])
        else:
            k[i][w]=k[i-1][w]
print(k[n][m])        