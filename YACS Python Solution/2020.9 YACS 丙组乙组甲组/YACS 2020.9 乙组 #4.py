'''
标准输出: 3 
5 69
4 1
1 2
4 2
4 3
0 4
标准输出: 6 
7 96
1 5
0 1
1 2
4 5
4 5
0 4
0 4

标准输出: 3 
输入: 
10 75
1 3
2 2
2 5
4 4
2 4
4 4
1 4
2 5
3 5
1 3
'''

n,T = map(int,input().split())
sellor = []
for i in range(n):
    sellor.append(list(map(int,input().split())))

# 未优化
dp = [[0]*(T) for _ in range(n)]

for i in range(n):
    for t in range(T):
        if T-sellor[i][0]*t-sellor[i][1]<0:
            dp[i][t] = dp[i-1][t-1]
        else:
            dp[i][t] = max(dp[i - 1][t - sellor[i][0]*t-sellor[i][1] - 1] + 1,dp[i - 1][t])
print(dp[n-1][T-1]+1)

# 空间优化
# ans = set()
# def dfs(visited,t):
#     t+=1
#     if t>T:
#         ans.add(len(visited)-1)
#         return None
#     if len(visited)==n: 
#         ans.add(n)
#         return
#     for i in range(n):
#         if not i in visited:
#             visited.add(i)
#             dfs(visited,t+sellor[i][0]*t+sellor[i][1])
#             visited.remove(i)
    
# dfs(set(),0)
# print(max(ans))