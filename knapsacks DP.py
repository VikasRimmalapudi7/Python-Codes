p=[0,1,2,5,6]
wt=[0,2,3,4,5]
m,n=8,5
k=[ [0 for i in range(m+1)]for j  in range(n+1)]
for i in range(n+1):   #columns
    for w in range(m+1):#rowss
        if i==0 or w==0:
            k[i][w]=0
        elif wt[i-1]<=w:
            k[i][w]=max((p[i-1]+k[i-1][w-wt[i-1]]),k[i-1][w])
        else:
            k[i][w]=k[i-1][w]    
print(k[n][w])
print(k)  #tabulation method
#now to see which elements are include we will iterate
i,j=n,m
while i>0 and j>0:
    if k[i][j]==k[i-1][j]:
        print(0)
        i-=1
    else:
        print(1)
        i-=1
        j-=wt[i] 

