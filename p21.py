s1 = "aabcc"
s2 = "dbbca" 
s3 = "aadbbcbcac"

l = len(s1)
m = len(s2)
n = len(s3)
if l + m != n:
            print(False)

dp = [[False for _ in range(m+1)] for _ in range(l+1)]       
dp[-1][-1] = True


for i in range(l, -1, -1):
            for j in range(m, -1, -1):
                if i < l and s1[i] == s3[i+j]:
                    dp[i][j] |= dp[i+1][j]

                if j < m and s2[j] == s3[i+j]:
                    dp[i][j] |= dp[i][j+1]
print(dp[0][0])