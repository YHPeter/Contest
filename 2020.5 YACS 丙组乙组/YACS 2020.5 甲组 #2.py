# YACS 2020.5 甲组 #2
# 汉堡与三明治
# sample answer from https://iai.sh.cn/contribution/96
mod = 10007
inv_2 = 5004
ans = 0
dp = [[0]*2200 for _ in range(2200)]
n,a,b = map(int,input().split(' '))
n-=1		
dp[a][b] = 1
i,j = a,b
for i in range(a,-1,-1):
    if a+b-i-j>n: continue
    for j in range(b,-1,-1):
        if a+b-i-j>n: continue
        elif i>0 and j>0:
            dp[i - 1][j] = (dp[i - 1][j] + inv_2 * dp[i][j]) % mod
            dp[i][j - 1] = (dp[i][j - 1] + inv_2 * dp[i][j]) % mod
        elif i > 0: dp[i - 1][j] = (dp[i - 1][j] + dp[i][j]) % mod
        elif j > 0: dp[i][j - 1] = (dp[i][j - 1] + dp[i][j]) % mod
for i in range(n+1):
    if a-i<=0 or b-n+i<0: continue
    elif b - n + i == 0: ans = (ans + dp[a - i][0]) % mod
    else: ans = (ans + inv_2 * dp[a - i][b - n + i]) % mod;
print(ans)