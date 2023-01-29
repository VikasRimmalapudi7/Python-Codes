n=9999999
dp=[1 for i in range(n+1)]
dp[0]=0
for i in range(2,n+1):
           for j in range(1,(n//i)+1):
               dp[i*j]=(abs(dp[i*j]-1))
                        
                        
ss=sum(dp)
print(ss)               