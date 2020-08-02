# 甲组 2020年4月
# 1. 神奇宝贝
# sample answer from https://iai.sh.cn/contribution/61

a,b = [0]*82,[0]*82
n,m = map(int,input().split(' '))
for i in range(1,n+1):
    a[i],b[i]= map(int,input().split(' '))
ans = 0
dp = [[[0]*40010 for _ in range(82)] for _ in range(2)]
dp[0][0][0] = 1
for i in range(1,n+1):
    for j in range(min(i,m)+1):
        for k in range(0,40002):
            now = i & 1
            pre = (i - 1) & 1
            dp[now][j][k] = dp[pre][j][k]
            if j > 0 and k >= b[i] and dp[pre][j - 1][k - b[i]]:
                dp[now][j][k] = max(dp[now][j][k],dp[pre][j - 1][k - b[i]] + a[i] * (k - b[i] + 1))
            ans = max(ans,dp[now][j][k])
print(ans-1)

# 2.运输
# sample answer from https://iai.sh.cn/contribution/71
def dfs(l,r,value):
    if l==0:
        if dp[r]>0 :
            dp[r+value] = max(dp[r+value],dp[r]+1)
        return
    x = l-(l&l-1)
    dfs(l - x,r,value)
    dfs(l - x,r + x,value)
# l：尚未考虑元素的压缩状态。
# r：考虑后的子集状态。
# 其实就是子集生成。 

n = int(input())
a = [0]+list(map(int,input().split(' ')))

dp = [0]*(20000100)
sum = [0]*(20000100)
to = {}
for i in range(22):
    to[1<<i] = i+1 # 辅助数组，快速求对数

N = (1 << n) - 1 # 辅助变量，表示全集状态

for i in range(1,N+1):
    x = i - (i & i - 1)
    sum[i] = sum[i - x] + a[to[x]]
    # 快速求集合元素和 
    
    if sum[i] == 0 and dp[i] == 0: #遇到不可拆分的零和集合 
        tmp = 1
        while tmp <= i :
            tmp = tmp << 1
        # 优化：可以只穷举比集合状态小的不相交集合 

        dfs(tmp - 1 - i,0,i)
        
        dp[i] = 1
    
print(n - dp[N]) # 注意是求min{n-m} 